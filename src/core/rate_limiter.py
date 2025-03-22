from slowapi import Limiter
from slowapi.util import get_remote_address
from src.core.config import Config


# Initialize rate limiter with redis storage
limiter = Limiter(
    key_func=get_remote_address,
    storage_uri=Config.REDIS_URL
)
