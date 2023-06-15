import requests

from config import settings
from db_management.db_commands import insert_streams_into_db
from models.stream import Stream

headers_token = {"Content-Type": "application/x-www-form-urlencoded"}
data = {
    "client_id": settings.CLIENT_ID,
    "client_secret": settings.CLIENT_SECRET,
    "grant_type": settings.GRANT_TYPE,
}
base_url = "https://api.twitch.tv/helix/streams?first=100"


async def parse_twitch():
    response = requests.post(
        "https://id.twitch.tv/oauth2/token", headers=headers_token, data=data
    ).json()
    access_token = "Bearer " + response.get("access_token")
    headers = {
        "Authorization": access_token,
        "Client-Id": "j0yobo10cfe37ajw4eipnu2dhjoxhy",
    }
    response2 = requests.get(
        base_url,
        headers=headers,
    ).json()
    cursor = response2.get("pagination").get("cursor")
    test_num = 3  # for testing
    for item in response2.get("data"):
        validated_object = dict(Stream.parse_obj(item))
        await insert_streams_into_db(validated_object)
    while test_num > 0:  # use here while cursor is not None
        response = requests.get(
            f"{base_url}&after={cursor}",
            headers=headers,
        ).json()
        for item in response.get("data"):
            validated_object = dict(Stream.parse_obj(item))
            await insert_streams_into_db(validated_object)
            cursor = response.get("pagination").get("cursor")
        test_num -= 1
