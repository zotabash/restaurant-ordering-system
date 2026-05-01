from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class OrderDetail(Base):

    __tablename__ = "order_details"

    order_item_id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    order_id = Column(
        Integer,
        ForeignKey("orders.order_id")
    )

    menu_item_id = Column(
        Integer,
        ForeignKey("menu_items.menu_item_id")
    )

    quantity = Column(
        Integer,
        nullable=False
    )

    order = relationship(
        "Order",
        back_populates="order_details"
    )

    sandwich = relationship(
        "Sandwich",
        back_populates="order_details"
    )