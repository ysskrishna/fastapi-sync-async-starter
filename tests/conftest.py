import os
import sys
# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import asyncio
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from fastapi.testclient import TestClient
from httpx import AsyncClient
from main import app
from src.core.database import Base
from src.core.database import get_db, get_async_db
from src.core.config import Config


# ----------------
# Shared Setup
# ----------------
test_engine = create_engine(Config.TEST_SQLALCHEMY_DATABASE_URL)
async_test_engine = create_async_engine(Config.TEST_ASYNC_SQLALCHEMY_DATABASE_URL)


TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
AsyncTestingSessionLocal = async_sessionmaker(async_test_engine, class_=AsyncSession, expire_on_commit=False)


# ----------------
# Database Setup
# ----------------
@pytest.fixture(autouse=True)
async def setup_database():
    Base.metadata.create_all(bind=test_engine)
    yield
    Base.metadata.drop_all(bind=test_engine)


# ----------------
# Synchronous Fixtures
# ----------------
@pytest.fixture(scope="session")
def engine():
    return test_engine


@pytest.fixture
def db_session():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()


    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()


# ----------------
# Asynchronous Fixtures
# ----------------
@pytest.fixture(scope="function")
async def async_engine():
    engine = create_async_engine(Config.TEST_ASYNC_SQLALCHEMY_DATABASE_URL)
    yield engine
    await engine.dispose()


@pytest.fixture
async def async_db_session(async_engine):
    async_session = async_sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session
        await session.rollback()
        await session.close()


@pytest.fixture
async def async_client(async_db_session):
    async def override_get_async_db():
        try:
            yield async_db_session
        finally:
            await async_db_session.close()


    app.dependency_overrides[get_async_db] = override_get_async_db
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
    app.dependency_overrides.clear()