from app.core.logger import logger
from app.agents.tutor import tutor_agent
from app.agents.quiz import quiz_agent
from app.rag.retriever import retrieve


async def handle_query(query: str):
    logger.info(f"Processing query: {query}")

    if "quiz" in query.lower():
        topic = query.lower().replace("quiz", "").strip()
        logger.info("Routing to Quiz Agent")
        return quiz_agent(topic)

    logger.info("Retrieving context from RAG...")
    context = retrieve(query)

    logger.info("Routing to Tutor Agent with RAG context")
    return tutor_agent(query, context)