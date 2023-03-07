import motor.motor_asyncio
import os
from dotenv import load_dotenv
from config import settings

load_dotenv()
conn = motor.motor_asyncio.AsyncIOMotorClient(settings.DATABASE_URL)
db = conn.college
collection = db.students
