from typing import Generator

from app.db.session import SessionLocal
from app.core.config import settings


search_path = settings.POSTGRES_SCHEMA

def get_db() -> Generator:
    try:
        db = SessionLocal()
        db.execute(f"SET search_path TO {search_path}")
        yield db
    finally:
        db.close()
