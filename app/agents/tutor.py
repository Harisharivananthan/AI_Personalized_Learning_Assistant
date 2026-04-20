from app.services.llm_service import generate_response
from app.core.logger import logger


def tutor_agent(query: str, context: str = ""):
    logger.info("Tutor agent activated")

    # If no context found
    if not context.strip():
        logger.warning("No RAG context found, falling back to LLM only")

    prompt = f"""
You are a helpful AI tutor.

Instructions:
- Explain clearly and simply
- Use the provided context if available
- If context is empty, answer from general knowledge

Context:
{context}

Question:
{query}
"""

    return generate_response(prompt)