import os
from dotenv import load_dotenv

load_dotenv()
class settings:
    OLLAMA_URL = os.getenv("OLLAMA_URL")
    MODEL = os.getenv("MODEL")
    REDIS_URL = os.getenv("REDIS_URL")
settings = settings()
