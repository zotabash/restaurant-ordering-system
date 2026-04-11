from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    customer_name = Column(String(100))

    description = Column(String(300))

    order_date = Column(
        DateTime,
        default=datetime.utcnow
    )

    order_details = relationship(
        "OrderDetail",
        back_populates="order"
    )