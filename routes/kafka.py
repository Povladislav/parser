from fastapi import APIRouter
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
import json
import asyncio
from parsing_lamoda import gather_data
from parsing_twitch import parse_twitch

route = APIRouter()

loop = asyncio.get_event_loop()
consumer = AIOKafkaConsumer("jobs", loop=loop, bootstrap_servers="kafka:9092")


@route.get('/create_task')
async def send(task: dict):
    producer = AIOKafkaProducer(loop=loop, bootstrap_servers="kafka:9092")
    await producer.start()
    try:
        print(f'Sending task...:')
        value_json = json.dumps(task).encode('utf-8')
        await producer.send_and_wait(topic="jobs", value=value_json)
    finally:
        await producer.stop()


async def consume():
    async for msg in consumer:
        message = json.loads(msg.value.decode())
        if message is not None:
            if message.get("parse_lamoda") is True:
                await gather_data()
            if message.get("parse_twitch") is True:
                await parse_twitch()
