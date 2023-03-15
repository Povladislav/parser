from typing import Optional

from fastapi import APIRouter, Depends

from configuration.db import db
from pagination.pagination import Pagination
from parsing_lamoda import parsing_through_pages_boots
from parsing_twitch import parse_twitch
from schemas.user import clothsEntity, streamsEntity

stream = APIRouter(prefix="/stream")

#1
@stream.post("/create")
async def create_streams():
    result = await parse_twitch()
    return {"success": True}


@stream.get("/get")
async def find_streams():
    result = await db.streams.find().to_list(10)
    return streamsEntity(result)


@stream.delete("/delete")
async def delete_stream_collection():
    await db.drop_collection("streams")
    return {"Deleted": True}
