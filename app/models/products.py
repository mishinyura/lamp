from sqlalchemy import Integer, String, Column, Numeric

from app.models.base import BaseModel, Base


class ProductModel(BaseModel, Base):
    __tablename__ = 'products'

    article = Column(String(20), nullable=False, unique=True)
    title = Column(String(150), nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    price = Column(Numeric(10, 2), nullable=False)
    image_url = Column(String, nullable=True)