from fastapi import APIRouter, Depends
from fastapi_app.core.security import admin_required

router = APIRouter(
    prefix="/ai",
    tags=["AI Assistant"]
)

@router.get("/")
def ai_status():
    return {"message": "AI API active"}

@router.get("/logs")
def get_admin_logs(admin=Depends(admin_required)):
    logs = list(db.admin_logs.find({}, {"_id": 0}).sort("timestamp", -1))
    return logs
