# SmartSupport AI – AI-Powered Customer Support Assistant

An AI-powered customer support application built with **Retrieval-Augmented Generation (RAG)**, local Large Language Models (LLMs), and semantic search.

SmartSupport AI retrieves relevant information from a customer FAQ knowledge base and generates context-aware answers using Ollama.

## Project Overview

SmartSupport AI demonstrates how Generative AI and RAG can be used to build an intelligent customer support assistant.

The application combines a Python-based RAG pipeline, ChromaDB vector database, Ollama local models, FastAPI backend, and Streamlit frontend.

## Features

- AI-powered customer support chatbot
- Retrieval-Augmented Generation (RAG)
- Local LLM integration using Ollama
- FAQ document processing
- Semantic search with ChromaDB
- Vector embeddings using Nomic Embed Text
- Answer generation using Llama 3.2
- REST API built with FastAPI
- Interactive chat interface built with Streamlit
- Context-based responses and fallback handling
- Docker and Docker Compose support

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Ollama | Local LLM execution |
| Llama 3.2 (3B) | Answer generation |
| Nomic Embed Text | Text embeddings |
| ChromaDB | Vector database |
| LangChain | LLM and RAG integration |
| FastAPI | Backend REST API |
| Streamlit | Frontend interface |
| Docker | Application containerization |
| Docker Compose | Multi-container orchestration |
| Git & GitHub | Version control |
## Application Screenshot

![SmartSupport AI Chatbot](screenshots/smart-support-ai-chatbot.png)
## Architecture

```text
                  Customer
                     |
                     v
              Streamlit UI
                Port 8501
                     |
                     v
                FastAPI
                Port 8000
                     |
                     v
                RAG Pipeline
                     |
             +-------+-------+
             |               |
             v               v
         ChromaDB          Ollama
       Vector Search     Local LLM
             |               |
             v               v
        Relevant FAQ     Generated Answer
             |               |
             +-------+-------+
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
│
├── api/
│   └── main.py
│
├── data/
│   └── raw/
│       └── customer_faq.txt
│
├── src/
│   ├── __init__.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── rag_pipeline.py
│
├── tests/
│   ├── test_api.py
│   └── test_rag.py
│
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
- Ollama running on the host Mac

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/mothadimanojkumar-alt/smart-support-ai.git

cd smart-support-ai
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Download Ollama models

Make sure Ollama is installed and running.

```bash
ollama pull llama3.2:3b

ollama pull nomic-embed-text
```

### 5. Build the vector database

```bash
python -m src.vector_store
```

## Run Locally

### Start the FastAPI backend

In the first terminal:

```bash
uvicorn api.main:app --reload
```

API documentation:

http://localhost:8000/docs

### Start the Streamlit frontend

In a second terminal:

```bash
streamlit run app.py
```

Open the application:

http://localhost:8501

## Run with Docker

Make sure Docker Desktop and Ollama are running on your Mac, and that the required Ollama models have been downloaded.

Build and start the containers:

```bash
docker compose up --build
```

The application uses the host Ollama service through:

```text
http://host.docker.internal:11434
```

Application endpoints:

| Service | URL |
|---|---|
| Streamlit Frontend | http://localhost:8501 |
| FastAPI Backend | http://localhost:8000 |
| API Documentation | http://localhost:8000/docs |

Stop the containers:

```bash
docker compose down
```

The ChromaDB data is stored in a Docker named volume called `chroma_data`, which is preserved when containers are stopped with the command above.

## Example Questions

Try asking the chatbot:

- How can I contact customer support?
- What are your business hours?
- How can I track my order?
- What is your return policy?
- How long does delivery take?
- What payment methods do you accept?

The assistant retrieves relevant information from the FAQ knowledge base and generates a response using the local language model.

## How It Works

1. A customer submits a question through the Streamlit interface.
2. Streamlit sends the question to the FastAPI backend.
3. The RAG pipeline generates an embedding for the question.
4. ChromaDB searches for relevant FAQ information.
5. The retrieved context is passed to Ollama.
6. Llama 3.2 generates a context-aware answer.
7. FastAPI returns the response to Streamlit.

## Testing

The project includes test files for the API and RAG pipeline.

Run the tests using:

```bash
pytest -v
```

## Future Improvements

- Add support for PDF and additional document formats.
- Implement conversation history.
- Add user authentication.
- Improve evaluation of retrieval quality and answer accuracy.
- Deploy the application to a cloud platform.

## Author

Manoj Kumar Mothadi

M.Sc. Software Engineering and Management

GitHub: https://github.com/mothadimanojkumar-alt

Project Repository: https://github.com/mothadimanojkumar-alt/smart-support-ai

---

Developed as a portfolio project to explore Generative AI, RAG architectures, local LLM integration, Python backend development, and Docker-based application deployment.