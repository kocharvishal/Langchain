# Langchain Project

This repository contains a collection of projects and experiments using the LangChain framework for building LLM-powered applications. The workspace is organized into several subfolders, each focusing on different use cases and components.

## Folder Structure

- **agents/**: Contains agent-related notebooks, such as Wikipedia search and web-based document retrieval using LangChain tools.
- **api/**: FastAPI-based server and client for serving LLM-powered endpoints. Includes integration with Ollama and prompt templates.
- **chain/**: Notebooks and data for document retrieval and question answering, including PDF loaders and vector store usage.
- **chatbot/**: Streamlit-based chatbot using local LLMs (Ollama) and custom prompt templates.
- **groq/**: (Details not shown, but likely contains Groq-related LLM integrations.)
- **rag/**: Retrieval-Augmented Generation (RAG) experiments, including text and PDF loaders, and sample data for RAG pipelines.

## Key Features

- **Document Loading**: Load and process documents from PDFs, web pages, and plain text.
- **Text Splitting**: Use recursive character text splitters for chunking documents.
- **Vector Stores**: Store and retrieve document embeddings using FAISS and ChromaDB.
- **LLM Integration**: Use Ollama (local LLM) and OpenAI-compatible models for chat and completion tasks.
- **API & UI**: FastAPI server for LLM endpoints and Streamlit UI for interactive chat and essay generation.
- **RAG Pipelines**: End-to-end retrieval and generation workflows for answering questions from custom corpora.

## Requirements

All dependencies are listed in `requirements.txt`. Install them with:

```powershell
pip install -r requirements.txt
```

## Getting Started

1. Clone the repository and install dependencies.
2. Start the FastAPI server from the `api/` folder:
   ```powershell
   uvicorn api.app:app --reload
   ```
3. Run the Streamlit chatbot from the `chatbot/` folder:
   ```powershell
   streamlit run chatbot/localama.py
   ```
4. Explore the notebooks in `agents/`, `chain/`, and `rag/` for more examples.

## Notes
- Make sure you have Ollama and any required LLM models installed locally.
- Environment variables can be set in a `.env` file for API keys and configuration.

---

**Last updated:** May 28, 2025
