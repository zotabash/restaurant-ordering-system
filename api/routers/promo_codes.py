from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import promo_codes as controller
from ..schemas.promo_codes import PromoCodeCreate, PromoCodeUpdate, PromoCode
from ..dependencies.database import get_db

router = APIRouter(prefix="/promos", tags=["Promo Codes"])

@router.post("/", response_model=PromoCode)
def create(request: PromoCodeCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/")
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{promo_id}", response_model=PromoCode)
def read_one(promo_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, promo_id)

@router.put("/{promo_id}", response_model=PromoCode)
def update(promo_id: int, request: PromoCodeUpdate, db: Session = Depends(get_db)):
    return controller.update(db, promo_id, request)

@router.delete("/{promo_id}")
def delete(promo_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, promo_id)
