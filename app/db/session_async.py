# app/db/session_async.py
from __future__ import annotations

from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.core.config import settings

DB_URL: str = settings.database_url

engine = create_async_engine(
    DB_URL,
    future=True,
    pool_pre_ping=True,
    echo=False,
)

SessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """FastAPI dependency (async)."""
    async with SessionLocal() as session:
        yield session