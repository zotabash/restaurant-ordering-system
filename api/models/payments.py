from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    amount = Column(DECIMAL(10, 2))
    method = Column(String(50))
    status = Column(String(50), default="pending")
    paid_at = Column(DateTime, default=datetime.utcnow)

    order = relationship("Order", back_populates="payments")
