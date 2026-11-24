
from pathlib import Path

import chromadb
import ollama
import os


# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# FAQ file location
FAQ_FILE = BASE_DIR / "data" / "raw" / "customer_faq.txt"

# ChromaDB database location
DB_PATH = BASE_DIR / "chroma_db"

# Model used to generate embeddings
EMBEDDING_MODEL = "nomic-embed-text"
OLLAMA_CLIENT = ollama.Client(
    host=os.getenv("OLLAMA_HOST", "http://localhost:11434")
)


def load_faq_documents():
    """Read FAQ information from the text file."""

    with open(FAQ_FILE, "r", encoding="utf-8") as file:
        content = file.read()

    # Separate individual FAQs using blank lines
    documents = [
        item.strip()
        for item in content.split("\n\n")
        if item.strip()
    ]

    return documents


def create_vector_store():
    """Convert FAQs into embeddings and store them in ChromaDB."""

    documents = load_faq_documents()

    # Generate embeddings using Ollama
    embeddings = []

    for document in documents:
        response = OLLAMA_CLIENT.embed(
    model=EMBEDDING_MODEL,
    input=document
)
        
        embeddings.append(response["embeddings"][0])

    # Create a persistent ChromaDB database
    client = chromadb.PersistentClient(path=str(DB_PATH))

    collection = client.get_or_create_collection(
        name="customer_faq"
    )

    # Store FAQ documents and their embeddings
    collection.upsert(
        ids=[f"faq_{i}" for i in range(len(documents))],
        documents=documents,
        embeddings=embeddings
    )

    print("FAQ documents stored successfully!")
    print("Total documents:", len(documents))
    print("Database location:", DB_PATH)


if __name__ == "__main__":
    create_vector_store()
