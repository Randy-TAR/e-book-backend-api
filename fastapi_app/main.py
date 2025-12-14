from fastapi import FastAPI
from .routers import books, blogs, ai_agent, analytics, admin


app = FastAPI(
    title="E-Book & Blog API",
    version="1.0"
)

# register routers
app.include_router(books.router, prefix="/books")
app.include_router(blogs.router, prefix="/blogs")
app.include_router(ai_agent.router)
app.include_router(analytics.router)
app.include_router(admin.router)
app.include_router(ai_agent.router, prefix="/ai")

@app.get("/")
def root():
    return {"message": "FastAPI backend running successfully!"}
