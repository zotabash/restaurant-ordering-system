from api.dependencies.database import Base, engine

from .orders import Order
from .order_details import OrderDetail
from .sandwiches import Sandwich
from .recipes import Recipe
from .resources import Resource


def index():
    Base.metadata.create_all(bind=engine)

