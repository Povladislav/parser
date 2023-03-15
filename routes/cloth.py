from typing import Optional

from fastapi import APIRouter, Depends

from configuration.db import db
from pagination.pagination import Pagination
from parsing_lamoda import parsing_through_pages_boots
from parsing_twitch import parse_twitch
from schemas.user import clothsEntity, streamsEntity

cloth = APIRouter(prefix="/cloth")


@cloth.get("/get")
async def find_all_cloths(pagination: Pagination = Depends()):
    cloths = await pagination.paginate()
    return clothsEntity(cloths)


@cloth.post("/create")
async def create_cloths():
    # await parsing_through_pages_cloths()
    await parsing_through_pages_boots()
    return {"success": True}


@cloth.delete("/delete")
async def delete_cloths_collection():
    await db.drop_collection("clothes")
    return {"Deleted": True}
