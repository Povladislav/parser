from typing import List

from fastapi import APIRouter, Depends

from configuration.db import db
from models.cloth import Cloth
from parsing_lamoda import parsing_through_pages_cloths, parsing_through_pages_boots
from schemas.user import clothEntity, clothsEntity

user = APIRouter()


@user.get("/")
async def find_all_cloths():
    cloths = await db.clothes.find().to_list(100)
    return clothsEntity(cloths)


@user.post("/")
async def create_cloths():
    # await parsing_through_pages_cloths()
    await parsing_through_pages_boots()
    return {"success": True}


@user.delete("/")
async def delete_collection():
    await db.drop_collection("clothes")
    return {"Deleted": True}
