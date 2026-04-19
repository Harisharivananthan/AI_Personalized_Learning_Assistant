from app.services.llm_service import generate_response
from app.core.logger import logger

async def handle_query(query: str):
    logger.info(f"Received query: {query}")
    response = generate_response(query)
    logger.info(f"Generated response: {response}")
    return response
