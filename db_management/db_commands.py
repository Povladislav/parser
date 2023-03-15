from configuration.db import db
from models.cloth import Cloth


async def insert_cloth_into_db(cloth: dict):
    await db.clothes.insert_one(cloth)


async def insert_boots_into_db(cloth: dict):
    await db.clothes.insert_one(cloth)


async def insert_streams_into_db(stream):
    item = await db.streams.insert_one(stream)
    # item_from_db = await db.streams.find_one({"_id": item.inserted_id})
    # return item_from_db
