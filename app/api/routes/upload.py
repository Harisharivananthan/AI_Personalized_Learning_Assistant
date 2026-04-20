from fastapi import APIRouter, UploadFile, File, BackgroundTasks
import os

from app.services.ingestion_service import process_pdf
from app.db.session import SessionLocal
from app.db.crud import save_document

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/pdf")
async def upload_pdf(file: UploadFile = File(...), background_tasks: BackgroundTasks = None):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Save metadata
    db = SessionLocal()
    save_document(db, file.filename)
    db.close()

    # Background processing
    background_tasks.add_task(process_pdf, file_path)

    return {
        "status": "processing started",
        "file": file.filename
    }