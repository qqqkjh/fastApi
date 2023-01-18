from sqlalchemy.orm import Session
from app import models
from app import schemas


def get_big_data_input(db: Session, idx: int):
    return db.query(models.BigDataInput).filter(models.BigDataInput.idx == idx).first()


def create_big_data_input(db: Session, item: schemas.BigDataInputCreate):
    db_item = models.BigDataInput(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
