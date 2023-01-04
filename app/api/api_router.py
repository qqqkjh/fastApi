from fastapi import APIRouter
from app.api.endpoints import color

api_router = APIRouter()

# 여기에 API 추가
api_router.include_router(color.router, tags=["color"])
