from sqlalchemy import Column, Integer, ForeignKey

from app.models.base import BaseModel, Base


class OrderToProductModel(BaseModel, Base):
    __tablename__ = 'orders_products'

    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
