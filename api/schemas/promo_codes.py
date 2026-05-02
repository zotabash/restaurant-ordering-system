from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PromoCodeBase(BaseModel):
    code: str
    discount_percent: float
    expires_at: datetime

class PromoCodeCreate(PromoCodeBase):
    pass

class PromoCodeUpdate(BaseModel):
    discount_percent: Optional[float] = None
    expires_at: Optional[datetime] = None
    active: Optional[bool] = None

class PromoCode(PromoCodeBase):
    id: int
    active: bool
    class Config:
        from_attributes = True
