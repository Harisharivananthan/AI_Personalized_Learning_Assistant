from fastapi import FastAPI
from app.api.routes import chat

app = FastAPI(title="AI Learning Assistant")

app.include_router(chat.router, prefix="/chat")

@app.get("/")
def root():
    return {"message": "API is running"}