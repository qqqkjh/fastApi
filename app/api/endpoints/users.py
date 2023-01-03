from fastapi import APIRouter

router = APIRouter()

@router.get("/user")
def user():
    return {"message": "this user Domain"}


