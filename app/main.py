from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from app.db import engine, async_session, Base
from app import models, schemas
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()

# Create the tables on startup (for demo, in prod use migrations)
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Dependency
async def get_db():
    async with async_session() as session:
        yield session

@app.post("/users/", response_model=schemas.UserRead, status_code=status.HTTP_201_CREATED)
async def register_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    # API-level validation: Check for existing email first
    result = await db.execute(select(models.User).where(models.User.email == user.email))
    existing_user = result.scalar_one_or_none()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered.")
    new_user = models.User(email=user.email, name=user.name)
    db.add(new_user)
    try:
        await db.commit()
        await db.refresh(new_user)
        return new_user
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Email already registered (at database level).")

@app.get("/users/", response_model=list[schemas.UserRead])
async def list_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.User))
    users = result.scalars().all()
    return users
