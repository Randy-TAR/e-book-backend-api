from datetime import datetime
from shared.db.mongo_client import db

def log_admin_action(admin, action: str, resource_id: str | None = None):
    db.admin_logs.insert_one({
        "admin_id": str(admin.get("user_id")),
        "username": admin.get("username"),
        "action": action,
        "resource_id": resource_id,
        "timestamp": datetime.utcnow()
    })
