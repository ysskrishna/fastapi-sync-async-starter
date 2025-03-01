from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models import models, schemas
from src.core.database import get_async_db


router = APIRouter(
    prefix="/async/users",
    tags=["async-users"]
)


@router.post("/", response_model=schemas.User)
async def create_user_async(user: schemas.UserCreate, db: AsyncSession = Depends(get_async_db)):
    # Check if user with email already exists
    result = await db.execute(
        select(models.User).filter(models.User.email == user.email)
    )
    existing_user = result.scalar_one_or_none()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")


    db_user = models.User(email=user.email, name=user.name)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


@router.get("/", response_model=list[schemas.User])
async def read_users_async(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_db)):
    result = await db.execute(
        select(models.User).offset(skip).limit(limit)
    )
    users = result.scalars().all()
    return users