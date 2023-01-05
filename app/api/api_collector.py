from fastapi import APIRouter
from app.api.endpoints import color, users

api_router = APIRouter()

# 여기에 API 추가
api_router.include_router(color.router, tags=["color"])
api_router.include_router(users.router, tags=["users"])
