from pydantic import BaseModel, ConfigDict


class ProductSchema(BaseModel):
    id: int
    article: str
    title: str
    stock: int
    price: float
    image_url: str

    model_config = ConfigDict(from_attributes=True)


class ProductCreateSchema(BaseModel):
    article: str
    title: str
    stock: int
    price: float
    image_url: str


class ProductAddCartSchema(BaseModel):
    article: str
    amount: int
