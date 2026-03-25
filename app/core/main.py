from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="AI ChatOps Assistant",
    description="AI-powered incident investigation service",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "chatops-assistant",
        "time": datetime.utcnow()
    }

@app.post("/chat")
def chat():
    return {
        "response": "Analyzing system logs..."
    }