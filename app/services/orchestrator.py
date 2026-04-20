from app.core.logger import logger
from app.agents.tutor import tutor_agent
from app.agents.quiz import quiz_agent
from app.rag.retriever import retrieve

from app.db.session import SessionLocal
from app.db.crud import save_chat
from app.services.llm_service import stream_response


def build_prompt(query: str, context: str, use_rag: bool):
    if use_rag:
        return f"""
You are a helpful AI tutor.

Use ONLY the context below to answer.

Context:
{context}

Question:
{query}
"""
    else:
        return f"""
You are a helpful AI tutor.

Answer clearly.

Question:
{query}
"""


async def handle_query(query: str):
    logger.info(f"Processing query: {query}")

    db = SessionLocal()

    try:
        if "quiz" in query.lower():
            topic = query.lower().replace("quiz", "").strip()
            response = quiz_agent(topic)

            save_chat(db, query, response)
            return response

        context_list = retrieve(query)
        context = "\n".join(context_list) if context_list else ""

        context_lower = context.lower()
        keywords = ["python", "function", "loop", "list", "tuple", "dictionary"]
        is_relevant = any(word in context_lower for word in keywords)

        if context and is_relevant:
            logger.info("Using RAG pipeline")
            response = tutor_agent(query, context=context, use_rag=True)
        else:
            logger.warning("Fallback to LLM")
            response = tutor_agent(query, context="", use_rag=False)

        save_chat(db, query, response, context)

        return response

    finally:
        db.close()


async def handle_query_stream(query: str):
    logger.info(f"Streaming query: {query}")

    context_list = retrieve(query)
    context = "\n".join(context_list) if context_list else ""

    context_lower = context.lower()
    keywords = ["python", "function", "loop", "list", "tuple", "dictionary"]
    is_relevant = any(word in context_lower for word in keywords)

    use_rag = bool(context and is_relevant)

    if use_rag:
        logger.info("Streaming RAG mode")
    else:
        logger.info("Streaming LLM fallback")

    prompt = build_prompt(query, context, use_rag)

    return stream_response(prompt)