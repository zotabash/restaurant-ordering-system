from .orders import Order
from .order_details import OrderDetail
from .sandwiches import Sandwich   # ← ADD THIS

from ..dependencies.database import Base, engine


def index():
    Base.metadata.create_all(bind=engine)

