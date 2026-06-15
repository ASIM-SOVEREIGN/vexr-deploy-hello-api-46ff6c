from fastapi import FastAPI
import httpx
from datetime import datetime

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from VEXR!", "time": datetime.now().isoformat()}

@app.get("/health")
def health():
    return {"status": "alive"}
