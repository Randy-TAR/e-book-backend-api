from fastapi import FastAPI
from routers import ai

app = FastAPI(title="AI Microservice")

app.include_router(ai.router)


@app.get("/")
def root():
    return {"status": "AI service running"}
