from app.rag.embedder import get_embedding
from app.rag.vector_store import search

def retrieve(query: str):
    vec = get_embedding(query)
    docs = search(vec)

    return "\n".join(docs)