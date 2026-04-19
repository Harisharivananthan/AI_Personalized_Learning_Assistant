from app.services.llm_service import generate_response
from app.core.logger import logger
from app.agents.tutor import tutor_agent
from app.agents.quiz import quiz_agent

async def handle_query(query: str):
    logger.info(f"Processing query: {query}")

    if "quiz" in query.lower():
        topic = query.replace("quiz", "")
        return quiz_agent(topic)

    return tutor_agent(query)