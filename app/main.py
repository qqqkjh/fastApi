from fastapi import FastAPI
from fastapi.responses import FileResponse
from .routers import color

app = FastAPI()
app.include_router(color.router)

favicon_path = 'favicon.ico'


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)
