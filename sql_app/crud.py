from sqlalchemy.orm import Session

from . import models, schemas

# Vehicle


def get_vehicles(db: Session):
    return db.query(models.Vehicle).all()


def get_vehicle(db: Session, vehicle_id: int):
    return db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()


def create_vehicle(db: Session, payload: schemas.Vehicle):
    db_item = models.Vehicle(**payload.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_vehicle(db: Session, vehicle_id: int):
    db_item = db.query(models.Vehicle).filter(
        models.Vehicle.id == vehicle_id).first()
    db.delete(db_item)
    db.commit()
    return db_item

# Question


def get_questions_by_vehicle_id(db: Session, vehicle_id: int):
    return (db.query(models.Question.id, models.Question.question, models.Question.frequency_check)
            .select_from(models.Question)
            .join(models.CategoryQuestion)
            .join(models.Category)
            .join(models.Vehicle)
            .filter(models.Vehicle.id == vehicle_id)
            .all()
            )

# Checklog


def get_checklogs(db: Session):
    return db.query(models.CheckLog).all()


def get_checklog(db: Session, checklog_id: int):
    return db.query(models.CheckLog).filter(models.CheckLog.id == checklog_id).first()


def create_check_log(db: Session, payload: schemas.CheckLog):
    db_item = models.CheckLog(**payload.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_checklog(db: Session, checklog_id: int):
    db_item = db.query(models.CheckLog).filter(
        models.CheckLog.id == checklog_id).first()
    db.delete(db_item)
    db.commit()
    return db_item


# Answer
