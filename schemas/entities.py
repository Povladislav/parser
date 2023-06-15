def clothEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "category": item["category"],
        "name": item["name"],
        "price": item["price"],
    }


def clothsEntity(entity) -> list:
    return [clothEntity(item) for item in entity]


def streamEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "user_id": str(item["user_id"]),
        "user_name": str(item["user_name"]),
        "game_id": str(item["game_id"]),
        "game_name": str(item["game_name"]),
        "type": str(item["type"]),
        "language": str(item["language"]),
        "is_mature": str(item["is_mature"]),
    }


def streamsEntity(entity) -> list:
    return [streamEntity(item) for item in entity]
