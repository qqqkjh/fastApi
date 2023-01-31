from fastapi import APIRouter
from app.api.endpoints import checks, big_data

api_router = APIRouter()

# 여기에 API 추가
api_router.include_router(big_data.router, tags=["big_data"])
api_router.include_router(checks.router, tags=["checks"])
