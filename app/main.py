from fastapi import FastAPI

app = FastAPI(title="Webhook Engine API")

@app.get("/health")
async def health_check():
    return {"status": "ok"}