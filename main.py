import asyncio
import json

import uvicorn
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_utils.tasks import repeat_every

from exceptions_controller.exep_controller import UnicornException
from routes.cloth import cloth
from routes.kafka import consume, consumer, route, send
from routes.stream import stream

app = FastAPI()
app.include_router(cloth)
app.include_router(stream)
app.include_router(route)


# PERIODIC TASKS
@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=404,
        content={
            "message": f"Oops! {exc.page} is not available! User positive page number!"
        },
    )


# @app.on_event("startup")
# async def startup_event():
#     await consumer.start()
#
#
# @app.on_event("startup")
# @repeat_every(seconds=100 * 100)
# async def create_task():
#     message = {
#         "parse_lamoda": True,
#         "parse_twitch": True
#     }
#     await send(message)
#
#
# @app.on_event("shutdown")
# async def startup_event():
#     await consumer.stop()

# if __name__ == "__main__":
#     uvicorn.run("parser.main:app", host="0.0.0.0", port=8000, reload=True)
