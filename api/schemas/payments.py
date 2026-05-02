from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PaymentBase(BaseModel):
    order_id: int
    amount: float
    method: str

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    method: Optional[str] = None
    status: Optional[str] = None

class Payment(PaymentBase):
    id: int
    status: str
    paid_at: datetime
    class Config:
        from_attributes = True
