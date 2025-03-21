from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.core.database import engine
from src.models import models
from src.routers import user_sync, user_async
from src.core.config import Config
from src.core.rate_limiter import limiter
from slowapi import _rate_limit_exceeded_handler

if not Config.IS_TESTING:
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

# Add the Limiter middleware and exception handler to the app
app.state.limiter = limiter
app.add_exception_handler(429, _rate_limit_exceeded_handler)

@app.get("/")
async def root():
    return {"message": "FastAPI Application is running"}

@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)