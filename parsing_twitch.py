import requests

from config import settings
from db_management.db_commands import insert_streams_into_db

headers = {"Content-Type": "application/x-www-form-urlencoded"}
data = {
    "client_id": settings.CLIENT_ID,
    "client_secret": settings.CLIENT_SECRET,
    "grant_type": settings.GRANT_TYPE,
}


async def parse_twitch():
    response = requests.post(
        "https://id.twitch.tv/oauth2/token", headers=headers, data=data
    ).json()
    access_token = "Bearer " + response.get("access_token")
    response2 = requests.get(
        "https://api.twitch.tv/helix/streams?first=1",
        headers={
            "Authorization": access_token,
            "Client-Id": "j0yobo10cfe37ajw4eipnu2dhjoxhy",
        },
    ).json()
    item = response2.get("data")[0]
    await insert_streams_into_db(item)
