
import ollama

# Name of our embedding model
EMBEDDING_MODEL = "nomic-embed-text"


def generate_embedding(text: str):
    """
    Convert text into a numerical embedding.
    """

    response = ollama.embed(
        model=EMBEDDING_MODEL,
        input=text
    )

    return response["embeddings"][0]


# Test the embedding function
if __name__ == "__main__":
    sample_text = "Our customer support team is available Monday to Friday."

    embedding = generate_embedding(sample_text)

    print("Embedding generated successfully!")
    print("Embedding length:", len(embedding))
    print("First 5 values:", embedding[:5])
