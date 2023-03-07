from typing import List

from fastapi import APIRouter
from schemas.user import userEntity, usersEntity
from models.user import User
from configuration.db import conn, db

user = APIRouter()


@user.get('/')
async def find_all_users():
    students = await db.students.find().to_list(100)
    return usersEntity(students)


@user.post('/')
async def create_user(user: User):
    item = await db.students.insert_one(dict(user))
    item_from_db = await db.students.find_one({"_id": item.inserted_id})
    return userEntity(item_from_db)
