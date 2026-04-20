from app.services.llm_service import generate_response
from app.core.logger import logger


def tutor_agent(query: str, context: str = "", use_rag: bool = False):
    logger.info("Tutor agent activated")

    if use_rag:
        logger.info("RAG mode")

        prompt = f"""
You are a helpful AI tutor.

Use the context below to answer accurately.

Context:
{context}

Question:
{query}

Give a clear explanation.
"""
    else:
        logger.info("LLM fallback mode")

        prompt = f"""
You are a helpful AI tutor.

Answer the question clearly and simply using your own knowledge.

Question:
{query}
"""

    return generate_response(prompt)
