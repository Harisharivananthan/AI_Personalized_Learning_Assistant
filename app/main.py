from fastapi import FastAPI

app = FastAPI(title="AI Learning Assistant")

@app.get("/")
def root():
    return {"message": "API is running"}