import datetime

from pydantic import BaseModel


class Stream(BaseModel):
    id: str
    user_id: str
    user_login: str
    user_name: str
    game_id: str
    game_name: str
    type: str
    tags: list | None
    viewer_count: int
    started_at: datetime.datetime
    language: str
    thumbnail_url: str
    tag_ids: list | None
    is_mature: bool
