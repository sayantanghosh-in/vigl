from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return { "message": "Welcome to Vigl", "timestamp": datetime.now() }