from fastapi import APIRouter, Request
from src.core.rate_limiter import limiter
import time

router = APIRouter(
    prefix="/sync/rate-limited",
    tags=["sync-rate-limited"]
)


@router.get("/hello")
@limiter.limit("5/minute")
def hello_sync(request: Request):
    return {"message": "Hello from a synchronous endpoint!"}


@router.get("/hello/{id}")
@limiter.limit("10/minute")
def hello_sync_with_id(request: Request, id: int):
    return {"message": f"Hello from a synchronous endpoint! {id}"}

@router.get("/burst")
@limiter.limit("5/minute;10/hour")
def burst_limit(request: Request):
    return {"message": "Testing burst rate limiting"}

@router.get("/slow")
@limiter.limit("3/minute")
def slow_endpoint(request: Request):
    # Simulate slow processing
    time.sleep(2)
    return {"message": "This is a slow endpoint"}