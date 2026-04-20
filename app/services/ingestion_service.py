from app.rag.pdf_loader import load_pdf, chunk_text
from app.rag.embedder import get_embedding
from app.rag.vector_store import add_document, save
from app.core.logger import logger


def process_pdf(file_path: str):
    logger.info(f"Processing PDF: {file_path}")

    text = load_pdf(file_path)

    if not text.strip():
        logger.error("No text extracted from PDF")
        return "Failed"

    chunks = chunk_text(text)
    logger.info(f"Chunks created: {len(chunks)}")

    for chunk in chunks:
        vector = get_embedding(chunk)
        add_document(chunk, vector)

    save()

    logger.info("PDF processed and stored successfully")

    return f"{len(chunks)} chunks stored"