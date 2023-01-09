import os
import logging
import uvicorn

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.api.api_collector import api_router
from app.core.config import settings
from app.core.logging import log_http

# for Path
favicon_path = 'favicon.ico'

APP_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(APP_DIR)
load_dotenv(os.path.join(BASE_DIR, ".env"))


# for App
def create_app():
    _app = FastAPI()
    _app.include_router(api_router)
    _app.add_middleware(BaseHTTPMiddleware, dispatch=log_http)

    # off default log
    uvicorn_access = logging.getLogger("uvicorn.access")
    uvicorn_access.disabled = True

    return _app


app = create_app()


@app.get("/")
async def root():
    return {"message": "Hello World & Docker"}


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    path = os.path.join(APP_DIR, favicon_path)
    print(path)
    return FileResponse(path)


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
    print("\n-- play main for debug --")
    uvicorn.run('main:app', host="localhost", port=8000, reload=True, reload_dirs=["app"])
