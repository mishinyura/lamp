from sqlalchemy import Integer, String, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from product_service.models.base import BaseModel, Base


class ProductModel(BaseModel, Base):
    __tablename__ = 'products'

    article: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    image_url: Mapped[str] = mapped_column(String, nullable=True)