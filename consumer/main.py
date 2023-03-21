from fastapi import FastAPI
from routes.kafka import consume, consumer, send
from fastapi_utils.tasks import repeat_every
import asyncio

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await consumer.start()
    asyncio.create_task(consume())


@app.on_event("startup")
@repeat_every(seconds=100 * 100)
async def create_task():
    message = {
        "parse_lamoda": True,
        "parse_twitch": True
    }
    await send(message)


@app.on_event("shutdown")
async def startup_event():
    await consumer.stop()
