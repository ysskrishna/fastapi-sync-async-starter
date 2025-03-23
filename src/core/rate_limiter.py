from slowapi import Limiter
from slowapi.util import get_remote_address
from src.core.config import Config


# Initialize rate limiter with appropriate storage based on environment
storage_uri = "memory://" if Config.IS_TESTING else Config.REDIS_URL
limiter = Limiter(
    key_func=get_remote_address,
    storage_uri=storage_uri
)
