
from pathlib import Path

import chromadb
import ollama


BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "chroma_db"

EMBEDDING_MODEL = "nomic-embed-text"


def search_faq(question: str, number_of_results: int = 3):
    """Find the most relevant FAQ documents."""

    # Connect to the existing ChromaDB database
    client = chromadb.PersistentClient(path=str(DB_PATH))

    collection = client.get_collection(name="customer_faq")

    # Convert the customer's question into an embedding
    response = ollama.embed(
        model=EMBEDDING_MODEL,
        input=question
    )

    question_embedding = response["embeddings"][0]

    # Search for similar FAQ documents
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=number_of_results
    )

    return results["documents"][0]


if __name__ == "__main__":
    question = "When is customer support available?"

    answers = search_faq(question)

    print("\nCustomer question:", question)
    print("\nRelevant FAQ information:")

    for answer in answers:
        print("-", answer)
