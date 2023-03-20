from pydantic import BaseModel


class Cloth(BaseModel):
    category: str
    name: str
    price: str
