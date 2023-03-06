import os
from fastapi import FastAPI
import motor.motor_asyncio

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ.get("DATABASE_URL"))
db = client.college


@app.get("/")
def foo():
    return ({"Working": 1})
