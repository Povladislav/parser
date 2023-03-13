from configuration.db import db
from models.cloth import Cloth


async def insert_cloth_into_db(cloth: dict):
    await db.clothes.insert_one(cloth)


async def insert_boots_into_db(cloth: dict):
    await db.clothes.insert_one(cloth)
