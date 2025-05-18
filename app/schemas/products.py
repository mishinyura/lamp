from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: int
    article: str
    title: str
    stock: int
    price: float
    image_url: str
