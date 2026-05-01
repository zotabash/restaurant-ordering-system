from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class OrderBase(BaseModel):

    customer_id: Optional[int] = None
    order_date: Optional[datetime] = None
    tracking_number: Optional[str] = None
    status: Optional[str] = None
    total_price: Optional[float] = None
    promo_id: Optional[int] = None


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):

    customer_id: Optional[int] = None
    status: Optional[str] = None
    total_price: Optional[float] = None


class Order(OrderBase):

    order_id: int

    class Config:
        from_attributes = True