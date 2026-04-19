from app.services.llm_service import generate_response
from app.core.logger import logger

def quiz_agent(topic: str):
    logger.info(f"Quiz agent activated")
    prompt = f"""
    Generate three multiple choice questions on the topic: {topic}.
    Includde options and correct answer."""
    return generate_response(prompt)
