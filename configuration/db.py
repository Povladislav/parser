import os

import motor.motor_asyncio
from dotenv import load_dotenv

from config import settings

load_dotenv()
conn = motor.motor_asyncio.AsyncIOMotorClient(settings.DATABASE_URL)
db = conn.college
clothes = db.clothes
streams = db.streams
