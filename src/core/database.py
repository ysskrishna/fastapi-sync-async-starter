from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.core.config import Config


# Sync SQLAlchemy setup
engine = create_engine(Config.SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Async SQLAlchemy setup
async_engine = create_async_engine(Config.ASYNC_SQLALCHEMY_DATABASE_URL)
AsyncSessionLocal = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)


Base = declarative_base()


# Dependency for sync database sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Dependency for async database sessions
async def get_async_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()