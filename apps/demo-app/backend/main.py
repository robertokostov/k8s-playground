from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI()

@app.get("/utc-time")
def get_utc_time():
    utc_now = datetime.now(timezone.utc)
    return {"utc_time": utc_now.isoformat()}

@app.get("/health")
def health():
    return {"status": "ok"}