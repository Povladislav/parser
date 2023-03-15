from fastapi import APIRouter, Depends
from typing import Optional
from configuration.db import db
from parsing_lamoda import parsing_through_pages_boots
from schemas.user import clothsEntity
from pagination.pagination import Pagination

user = APIRouter()


@user.get("/")
async def find_all_cloths(pagination: Pagination = Depends()):
    cloths = await pagination.paginate()
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
