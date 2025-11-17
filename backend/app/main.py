from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(
    title="Data Syncer API",
    description="Backend API for the Python + Next data synchronization tool",
    version="0.1.0",
)


# Status model
class SyncStatus(BaseModel):
    status: str
    last_sync_at: datetime | None = None
    total_files: int | None = None
    changed_files: int | None = None


# Initial fake data (later replaced with real sync-engine output)
FAKE_STATUS = SyncStatus(
    status="idle", last_sync_at=None, total_files=0, changed_files=0
)


@app.get("/health")
def health_check():
    return {"ok": True, "message": "Data Syncer API is running"}


@app.get("/status", response_model=SyncStatus)
def get_status():
    return FAKE_STATUS
