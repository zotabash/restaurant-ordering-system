from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ReviewBase(BaseModel):
    order_id: int
    menu_item_id: int
    rating: int
    comment: Optional[str] = None

class ReviewCreate(ReviewBase):
    pass

class ReviewUpdate(BaseModel):
    rating: Optional[int] = None
    comment: Optional[str] = None

class Review(ReviewBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True
