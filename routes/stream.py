import json

from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from fastapi import APIRouter, Depends

from configuration.db import db
from pagination.pagination import Pagination
from parsing_twitch import parse_twitch
from exceptions_controller.exep_controller import UnicornException
from schemas.entities import streamsEntity

stream = APIRouter(prefix="/stream")


@stream.post("/create")
async def create_streams():
    await parse_twitch()
    return {"success": True}


@stream.get("/get")
async def find_streams(pagination: Pagination = Depends()):
    if pagination.page < 0:
        raise UnicornException(pagination.page)

    result = await pagination.paginate_streams()
    return streamsEntity(result)


@stream.delete("/delete")
async def delete_stream_collection():
    await db.drop_collection("streams")
    return {"Deleted": True}
