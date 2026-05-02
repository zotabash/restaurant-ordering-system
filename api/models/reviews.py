from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    menu_item_id = Column(Integer, ForeignKey("menu_items.menu_item_id"))
    rating = Column(Integer, nullable=False)
    comment = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow)

    order = relationship("Order", back_populates="reviews")
    menu_item = relationship("Sandwich", back_populates="reviews")
