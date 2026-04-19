import requests 
from app.core.config import settings
from app.core.logger import logger

def generate_response(prompt:str):
    try:
        logger.info("Sending request to ollama")
        response = requests.post(
            settings.OLLAMA_URL,
            json={
                "model":settings.MODEL,
                "prompt":prompt,
                "stream":False
            }
        )

        data = response.json()
        return data.get("response","no response")

    except Exception as e:
        logger.error(f"LLM error:{e}")
        return "LLM connection Failed"
        