from .orders import Order
from .order_details import OrderDetail
from .sandwiches import Sandwich   # ← ADD THIS
from .recipes import Recipe
from .resources import Resource
from .payments import Payment
from .reviews import Review
from .promo_codes import PromoCode
from ..dependencies.database import Base, engine


def index():
    Base.metadata.create_all(bind=engine)

