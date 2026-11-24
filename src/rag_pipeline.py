
from .retriever import search_faq
import ollama
import os


LLM_MODEL = "llama3.2:3b"
OLLAMA_CLIENT = ollama.Client(
    host=os.getenv("OLLAMA_HOST", "http://localhost:11434")
)


def generate_answer(question: str):
    """Generate an answer using retrieved FAQ information."""

    # Step 1: Retrieve relevant FAQ documents
    relevant_documents = search_faq(question)

    # Step 2: Combine retrieved information into context
    context = "\n\n".join(relevant_documents)

    # Step 3: Create instructions for the language model
    prompt = f"""
You are SmartSupport AI, a helpful customer support assistant.

Answer the customer's question using ONLY the information
provided in the context below.

If the answer is not available in the context,
say: "I'm sorry, I don't have that information."

Context:
{context}

Customer question:
{question}

Answer:
"""

    # Step 4: Generate the answer using Ollama
    
    response = OLLAMA_CLIENT.chat(
        model=LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )


    return response["message"]["content"]


if __name__ == "__main__":
    question = "When is customer support available?"

    answer = generate_answer(question)

    print("\nCustomer:", question)
    print("\nSmartSupport AI:", answer)
