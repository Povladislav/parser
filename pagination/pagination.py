from configuration.db import db


class Pagination:
    def __init__(self, page: int, items_on_page: int):
        self.page = page
        self.items_on_page = items_on_page

    async def paginate(self):
        list_items = []
        items_to_skip = (self.page - 1) * self.items_on_page
        async for item in db.clothes.find().limit(self.items_on_page).skip(
            items_to_skip
        ):
            list_items.append(item)
        return list_items
