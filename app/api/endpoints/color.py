from typing import Union
from fastapi import APIRouter
from app.enums import Color

router = APIRouter()

@router.get("/color/{user_color}", tags=["color"])
async def user(user_color: Union[Color, str]):

    print(user_color)

    if type(user_color) == Color:
        return {"message": user_color.value, "model": user_color.name, "enumCheck": True}

    return {"message": user_color, "model": user_color}
