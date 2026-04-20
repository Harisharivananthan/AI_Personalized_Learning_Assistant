import requests
import json
from app.core.config import settings
from app.core.logger import logger


def generate_response(prompt: str):
    """
    Standard (non-streaming) response
    """
    try:
        logger.info("Sending request to Ollama (sync)")

        response = requests.post(
            settings.OLLAMA_URL,
            json={
                "model": settings.MODEL,
                "prompt": prompt,
                "stream": False
            }
        )

        response.raise_for_status()
        data = response.json()

        return data.get("response", "No response")

    except Exception as e:
        logger.error(f"LLM error: {e}")
        return "LLM connection failed"


def stream_response(prompt: str):
    """
    Streaming response (token by token)
    """
    try:
        logger.info("Sending request to Ollama (stream)")

        with requests.post(
            settings.OLLAMA_URL,
            json={
                "model": settings.MODEL,
                "prompt": prompt,
                "stream": True
            },
            stream=True
        ) as response:

            response.raise_for_status()

            for line in response.iter_lines():
                if line:
                    try:
                        data = json.loads(line.decode("utf-8"))
                        yield data.get("response", "")
                    except Exception:
                        continue

    except Exception as e:
        logger.error(f"Streaming LLM error: {e}")
        yield "LLM streaming failed"