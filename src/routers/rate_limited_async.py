from fastapi import APIRouter, Request
from src.core.rate_limiter import limiter
import asyncio

router = APIRouter(
    prefix="/async/rate-limited",
    tags=["async-rate-limited"]
)


@router.get("/hello")
@limiter.limit("5/minute")
def hello_async(request: Request):
    return {"message": "Hello from an asynchronous endpoint!"}


@router.get("/hello/{id}")
@limiter.shared_limit("10/minute", scope="async_hello_with_id")
def hello_async_with_id(request: Request, id: int):
    return {"message": f"Hello from an asynchronous endpoint! {id}"}

@router.get("/burst")
@limiter.limit("5/minute;10/hour")
async def burst_limit(request: Request):
    return {"message": "Testing burst rate limiting"}

@router.get("/slow")
@limiter.limit("3/minute")
async def slow_endpoint(request: Request):
    # Simulate slow processing
    await asyncio.sleep(2)
    return {"message": "This is a slow endpoint"}