from fastapi import APIRouter
from app.services.orchestrator import handle_query

router = APIRouter()

@router.post("/")
async def chat(query: str):
    response = await handle_query(query)

    return {
        "response": response  
    }