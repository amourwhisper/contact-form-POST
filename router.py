from fastapi import FastAPI, Form, HTTPException
from typing import Annotated
from validation import ContactForm

app = FastAPI()

@app.post("/contact")
async def contact(
    name: Annotated[ContactForm, Form()],
    email: Annotated[ContactForm, Form()],
    message: Annotated[ContactForm, Form()]
):
    if not name:
        raise HTTPException(
            status_code=400, 
            detail="Name is required"
            )
    if not email:
        raise HTTPException(
            status_code=400, 
            detail="Email is required"
            )
    if not message:
        raise HTTPException(
            status_code=400, 
            detail="Message is required"
            )
    with open("contact_submissions.txt", "a") as f:
        f.write(
            f"Name: {name}/n"
            f"Email: {email}/n"
            f"Message: {message}/n"
            f"{'-'*30}/n"
        )
    return {
        "status": "success",
        "message": "Form submitted successfully"
    }
