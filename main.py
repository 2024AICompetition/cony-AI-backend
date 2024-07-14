from fastapi import FastAPI
import os
from dotenv import load_dotenv
from routers.v1.DiaryRouter import DiaryRouter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()

app.include_router(DiaryRouter)

@app.get("/")
async def root():
    return {"state": "activate"}
