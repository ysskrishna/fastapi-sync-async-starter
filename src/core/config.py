import os
from dotenv import load_dotenv

load_dotenv()



class Config:
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
   
    TEST_DB_HOST = os.getenv("TEST_DB_HOST")
    TEST_DB_PORT = os.getenv("TEST_DB_PORT")
    TEST_DB_USER = os.getenv("TEST_DB_USER")
    TEST_DB_PASSWORD = os.getenv("TEST_DB_PASSWORD")
    TEST_DB_NAME = os.getenv("TEST_DB_NAME")

    SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    ASYNC_SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
   
    TEST_SQLALCHEMY_DATABASE_URL = f"postgresql://{TEST_DB_USER}:{TEST_DB_PASSWORD}@{TEST_DB_HOST}:{TEST_DB_PORT}/{TEST_DB_NAME}"
    TEST_ASYNC_SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{TEST_DB_USER}:{TEST_DB_PASSWORD}@{TEST_DB_HOST}:{TEST_DB_PORT}/{TEST_DB_NAME}"