from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Sandwich(Base):

    __tablename__ = "menu_items"

    menu_item_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(String(100))

    price = Column(DECIMAL(10, 2))

    calories = Column(Integer)

    category = Column(String(50))

    order_details = relationship(
        "OrderDetail",
        back_populates="sandwich"
    )