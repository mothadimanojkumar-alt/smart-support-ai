
# 🤖 SmartSupport AI

An AI-powered customer support assistant that answers customer questions using Retrieval-Augmented Generation (RAG) and locally running Large Language Models.

## 🚀 Project Overview

SmartSupport AI is a Python-based customer support application designed to retrieve relevant information from company FAQ documents and generate accurate, context-aware answers.

The application uses Ollama to run the language model locally, ChromaDB to store and search document embeddings, FastAPI for backend services, and Streamlit for the interactive chat interface.

## ✨ Features

- AI-powered customer support chatbot
- Retrieval-Augmented Generation (RAG)
- Local LLM integration using Ollama
- FAQ document processing
- Semantic search using ChromaDB
- REST API using FastAPI
- Interactive chat interface using Streamlit
- Responses based on retrieved knowledge
- Fallback responses for unavailable information

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Ollama | Local language models and embeddings |
| Llama 3.2 | Answer generation |
| Nomic Embed Text | Text embeddings |
| ChromaDB | Vector database |
| FastAPI | Backend REST API |
| Streamlit | Frontend chat interface |
| Git & GitHub | Version control |

## 📁 Project Structure

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
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

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

### 4. Install Ollama models

Make sure Ollama is installed and running.

Pull the required models:

```bash
ollama pull llama3.2:3b

ollama pull nomic-embed-text
```

### 5. Build the vector database

```bash
python -m src.vector_store
```

## ▶️ Run the Application

### Start the FastAPI backend

Open the first terminal:

```bash
uvicorn api.main:app --reload
```

API documentation:

http://127.0.0.1:8000/docs

### Start the Streamlit frontend

Open a second terminal:

```bash
streamlit run app.py
```

Open the application:

http://localhost:8501

## 💬 Example Questions

- What are your business hours?
- How can I track my order?
- What is your return policy?
- How long does delivery take?
- What payment methods do you accept?
- Do you offer free international shipping?

The assistant retrieves relevant information from the FAQ knowledge base and responds using the language model.

## 🧠 How It Works

1. Customer submits a question through Streamlit.
2. Streamlit sends the question to FastAPI.
3. The RAG pipeline converts the question into an embedding.
4. ChromaDB retrieves relevant FAQ documents.
5. Ollama generates an answer using the retrieved context.
6. FastAPI returns the answer to Streamlit.

## 👨‍💻 Author

**Manoj Kumar Mothadi**

M.Sc. Software Engineering and Management

GitHub: https://github.com/mothadimanojkumar-alt

---

*Developed as a portfolio project to explore Generative AI, RAG architectures, Python backend development, and local LLM integration.*
