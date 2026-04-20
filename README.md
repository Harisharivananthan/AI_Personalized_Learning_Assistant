# 🎓 AI-Powered Learning Assistant (RAG + Agents)

## 🚀 Overview
This project is a GenAI-based learning assistant that provides tutoring, quiz generation, and contextual Q&A using LLMs and Retrieval-Augmented Generation (RAG).

## ✨ Features
- Tutor agent for explanations
- Quiz generation agent
- RAG-based semantic search (FAISS)
- Async document ingestion (Celery + Redis)
- Streaming responses
- Chat history storage (SQLite)

## 🧠 Architecture
User → FastAPI → Orchestrator → Agents → RAG → LLM → Response

## 🛠 Tech Stack
- Python, FastAPI
- FAISS, Sentence-Transformers
- Redis, Celery
- SQLite
- Ollama (Gemma LLM)

## ▶️ How to Run

1. Start Ollama:
   ollama run gemma

2. Start Redis:
   redis-server

3. Start Celery:
   celery -A app.workers.tasks worker --loglevel=info

4. Run API:
   uvicorn app.main:app --reload

5. Run UI:
   streamlit run frontend/app.py


## 📌 Future Improvements
- User authentication
- Multi-user support
- Better UI