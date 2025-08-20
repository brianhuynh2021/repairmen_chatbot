# app/db/session_sync.py
from __future__ import annotations

from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.core.config import settings

DB_URL: str = settings.database_url  # ví dụ: "sqlite:///./repairmen_local.db" hoặc "postgresql+psycopg2://..."

connect_args = {"check_same_thread": False} if DB_URL.startswith("sqlite") else {}

engine = create_engine(
    DB_URL,
    future=True,
    pool_pre_ping=True,
    connect_args=connect_args,
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_session() -> Generator[Session, None, None]:
    """FastAPI dependency (sync)."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()