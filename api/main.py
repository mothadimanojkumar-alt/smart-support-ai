
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.rag_pipeline import generate_answer


# Create the FastAPI application
app = FastAPI(
    title="SmartSupport AI API",
    description="AI-powered customer support API using RAG and Ollama",
    version="1.0.0"
)


# Define the customer question format
class CustomerQuestion(BaseModel):
    question: str


# Welcome endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to SmartSupport AI API!",
        "status": "running"
    }


# Customer support endpoint
@app.post("/ask")
def ask_question(request: CustomerQuestion):

    try:
        answer = generate_answer(request.question)

        return {
            "question": request.question,
            "answer": answer
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )
