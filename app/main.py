import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from app.api.api_collector import api_router

app = FastAPI()
app.include_router(api_router)

favicon_path = 'app/favicon.ico'


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    print(favicon_path)
    return FileResponse(favicon_path)


if __name__ == "__main__":
    print("--play main for debug--")
    uvicorn.run('main:app', host="localhost", port=8000,  reload=True, reload_dirs=["app"])
