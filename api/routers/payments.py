from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import payments as controller
from ..schemas.payments import PaymentCreate, PaymentUpdate, Payment
from ..dependencies.database import get_db

router = APIRouter(prefix="/payments", tags=["Payments"])

@router.post("/", response_model=Payment)
def create(request: PaymentCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/")
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{payment_id}", response_model=Payment)
def read_one(payment_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, payment_id)

@router.put("/{payment_id}", response_model=Payment)
def update(payment_id: int, request: PaymentUpdate, db: Session = Depends(get_db)):
    return controller.update(db, payment_id, request)

@router.delete("/{payment_id}")
def delete(payment_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, payment_id)
