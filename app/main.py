from fastapi import FastAPI
from app.api.routes import chat, upload
from app.db.session import engine, Base

app = FastAPI(title="AI Learning Assistant")

Base.metadata.create_all(bind=engine)
app.include_router(chat.router, prefix="/chat")
app.include_router(upload.router, prefix="/upload")

@app.get("/")
def root():
    return {"message": "API is running"}