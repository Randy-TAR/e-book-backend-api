from fastapi import FastAPI
from .routers import books, blogs, ai_agent, analytics

app = FastAPI(
    title="E-Book LMS API",
    version="1.0"
)

# register routers
app.include_router(books.router)
app.include_router(blogs.router)
app.include_router(ai_agent.router)
app.include_router(analytics.router)

@app.get("/")
def root():
    return {"message": "FastAPI backend running successfully!"}
