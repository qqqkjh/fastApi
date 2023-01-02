from typing import Union

from fastapi import FastAPI
from fastapi.responses import FileResponse
from enums import Color

app = FastAPI()
favicon_path = 'favicon.ico'


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/user/{user_id}")
async def user(user_id: int):
    return {"message": user_id}


@app.get("/color/{user_color}")
async def user(user_color: Union[Color, str]):

    print(user_color)

    if type(user_color) == Color:
        return {"message": user_color.value, "model": user_color.name, "enumCheck": True}

    return {"message": user_color, "model": user_color}


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)
