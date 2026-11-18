
from fastapi import FastAPI

app = FastAPI(
    title="Enterprise RAG Assistant",
    description="AI-powered enterprise knowledge assistant",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Enterprise RAG Assistant!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
