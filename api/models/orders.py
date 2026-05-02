from sqlalchemy import Column, Integer, String, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):

    __tablename__ = "orders"

    order_id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    customer_id = Column(Integer)

    order_date = Column(
        DateTime,
        default=datetime.utcnow
    )

    tracking_number = Column(
        String(100),
        unique=True
    )

    status = Column(
        String(50)
    )

    total_price = Column(
        DECIMAL(10, 2)
    )

    promo_id = Column(Integer)

    order_details = relationship(
        "OrderDetail",
        back_populates="order"
    )
    payments = relationship("Payment", back_populates="order")
    reviews = relationship("Review", back_populates="order")
