import os
import uvicorn

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse
from app.api.api_collector import api_router
from app.core.config import settings

app = FastAPI()
app.include_router(api_router)

favicon_path = 'app/favicon.ico'

APP_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(APP_DIR)
load_dotenv(os.path.join(BASE_DIR, ".env"))


@app.get("/")
async def root():
    return {"message": "Hello World & Docker"}


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    print(favicon_path)
    return FileResponse(favicon_path)


@app.get("/info")
async def info():
    return {"settings": settings}


@app.get("/check-dir")
async def check_dir():

    print(os.environ)
    print("====")
    print(settings)
    print("====")
    print(APP_DIR)
    print(BASE_DIR)
    print(os.environ.get("ADMIN_EMAIL"))

    return {"message": "Hello ser"}


if __name__ == "__main__":
    print("--play main for debug--")
    uvicorn.run('main:app', host="localhost", port=8000, reload=True, reload_dirs=["app"])
