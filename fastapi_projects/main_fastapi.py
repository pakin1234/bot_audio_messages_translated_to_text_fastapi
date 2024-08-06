from fastapi import FastAPI
from api.endpoints.file import router

app = FastAPI()
app.include_router(router, prefix="/file")

@app.get("/")
async def read_root():
    return {"data": "This is audio to text appliance"}