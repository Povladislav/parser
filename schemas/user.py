def clothEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "category": item["category"],
        "name": item["name"],
        "price": item["price"],
    }


def clothsEntity(entity) -> list:
    return [clothEntity(item) for item in entity]
