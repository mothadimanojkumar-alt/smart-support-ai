# SmartSupport AI – AI-Powered Customer Support Assistant

An AI-powered customer support chatbot built using Retrieval-Augmented Generation (RAG), local Large Language Models (LLMs), and semantic search.

SmartSupport AI retrieves relevant information from a customer FAQ knowledge base and generates context-aware answers using locally running Ollama models.

## Features

- AI-powered customer support chatbot
- Retrieval-Augmented Generation (RAG)
- Local LLM integration using Ollama
- Llama 3.2 (3B) for answer generation
- Nomic Embed Text for text embeddings
- Semantic search using ChromaDB
- REST API built with FastAPI
- Interactive chat interface built with Streamlit
- Context-based responses and fallback handling
- Docker and Docker Compose support

## Application Screenshot

![SmartSupport AI Chatbot](screenshots/smart-support-ai-chatbot.png)

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Application development |
| Ollama | Local LLM and embedding execution |
| Llama 3.2 (3B) | Answer generation |
| Nomic Embed Text | Text embeddings |
| ChromaDB | Vector database |
| LangChain | RAG and LLM integration |
| FastAPI | Backend REST API |
| Streamlit | Frontend chat interface |
| Docker | Application containerization |
| Docker Compose | Multi-container orchestration |
| Git & GitHub | Version control |

## Architecture

```text
Customer
   |
   v
Streamlit UI (Port 8501)
   |
   v
FastAPI (Port 8000)
   |
   v
RAG Pipeline
   |
   +------------------+
   |                  |
   v                  v
ChromaDB            Ollama
Vector Search       Local LLM
   |                  |
   v                  v
Relevant FAQ       Generated Answer
   |                  |
   +--------+---------+
            |
            v
      Final Response
            |
            v
         Customer
```

## Project Structure

```text
smart-support-ai/
├── api/
│   └── main.py
├── data/
│   └── raw/
│       └── customer_faq.txt
├── src/
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── rag_pipeline.py
├── tests/
│   ├── test_api.py
│   └── test_rag.py
├── app.py
├── requirements.txt
├── Dockerfile
├── compose.yaml
├── .dockerignore
├── .gitignore
└── README.md
```

## Prerequisites

For local execution:
- Python 3.12
- Ollama
- Git

For Docker execution:
- Docker Desktop
- Ollama running on the host machine
- Required Ollama models downloaded

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/mothadimanojkumar-alt/smart-support-ai.git
cd smart-support-ai
```

### 2. Create and activate a virtual environment

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Download Ollama models

```bash
ollama pull llama3.2:3b
ollama pull nomic-embed-text
```

### 5. Initialize the vector database

```bash
python -m src.vector_store
```

## Run Locally

Start the FastAPI backend in the first terminal:

```bash
uvicorn api.main:app --reload
```

Start the Streamlit frontend in a second terminal:

```bash
streamlit run app.py
```

Open the application:

- Frontend: http://localhost:8501
- API: http://localhost:8000
- API documentation: http://localhost:8000/docs

## Run with Docker

Make sure Docker Desktop and Ollama are running and the required models are downloaded.

Build and start the containers:

```bash
docker compose up --build
```

The Docker configuration connects to the host Ollama service using:

```text
http://host.docker.internal:11434
```

Application endpoints:

- Streamlit: http://localhost:8501
- FastAPI: http://localhost:8000
- API documentation: http://localhost:8000/docs

Stop the containers:

```bash
docker compose down
```

The ChromaDB data is stored in a Docker named volume called `chroma_data`, which is preserved when containers are stopped using the command above.

## Example Questions

Try asking the chatbot:

- How can I contact customer support?
- What are your business hours?
- How can I track my order?
- What is your return policy?
- How long does delivery take?
- What payment methods do you accept?

## How It Works

1. A customer submits a question through the Streamlit interface.
2. Streamlit sends the question to the FastAPI backend.
3. The RAG pipeline generates an embedding for the question.
4. ChromaDB searches for relevant FAQ information.
5. The retrieved context is passed to Ollama.
6. Llama 3.2 generates a context-aware answer.
7. FastAPI returns the response to Streamlit.

## Testing

The project includes automated tests for the API and RAG pipeline.

Run the tests:

```bash
python -m pytest -v
```

The current test suite contains five tests.

## Future Improvements

- Add support for PDF and additional document formats.
- Implement conversation history.
- Add user authentication.
- Improve retrieval and answer-quality evaluation.
- Deploy the application to a cloud platform.

## Author

**Manoj Kumar Mothadi**

M.Sc. Software Engineering and Management

GitHub: https://github.com/mothadimanojkumar-alt

Project Repository: https://github.com/mothadimanojkumar-alt/smart-support-ai

---

Developed as a portfolio project to explore Generative AI, RAG architectures, local LLM integration, Python backend development, and Docker-based application deployment.