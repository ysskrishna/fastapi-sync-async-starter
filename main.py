from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.core.database import engine
from src.models import models
from src.routers import user_sync, user_async

# create all tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Sync Async Starter", 
    description="A starter project for FastAPI with sync and async endpoints"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(user_sync.router)
app.include_router(user_async.router)

@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)