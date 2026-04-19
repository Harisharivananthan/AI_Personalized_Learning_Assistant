from app.services.llm_service import generate_response
from app.core.logger import logger

def tutor_agent(query: str):
    logger.info(f"Tutor agent activated")
    prompt = f"""
you are a helpful tutor.
Explain celerly and simply.
question: {query}"""
    return generate_response(prompt)