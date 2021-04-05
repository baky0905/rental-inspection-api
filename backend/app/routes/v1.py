# import uvicorn
from fastapi import Depends, HTTPException, APIRouter

from sqlalchemy.orm import Session
from typing import List
from app import crud, models, schemas
from app.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app_v1 = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Vehicle


@app_v1.get("/vehicles/", tags=["Vehicle"],   response_model=List[schemas.Vehicle])
def read_items(db: Session = Depends(get_db)):
    items = crud.get_vehicles(db)
    return items


@app_v1.get("/vehicle/{vehicle_id}", tags=["Vehicle"], response_model=schemas.Vehicle)
def read_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    vehicle = crud.get_vehicle(db, vehicle_id=vehicle_id)
    if vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle


@app_v1.post("/vehicle/", tags=["Vehicle"], response_model=schemas.Vehicle, status_code=201)
def write_vehicle(*, db: Session = Depends(get_db), payload: schemas.Vehicle):
    return crud.create_vehicle(db, payload=payload)


@app_v1.delete("/vehicle/{vehicle_id}", tags=["Vehicle"], response_model=schemas.Vehicle)
def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    vehicle = crud.get_vehicle(db, vehicle_id=vehicle_id)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    vehicle = crud.delete_vehicle(db, vehicle_id=vehicle_id)
    return vehicle


# Question


@app_v1.get("/questions/{vehicle_id}", tags=["Question"], response_model=List[schemas.Question])
def read_questions(vehicle_id: int, db: Session = Depends(get_db)):
    questions = crud.get_questions_by_vehicle_id(db, vehicle_id=vehicle_id)
    if len(questions) == 0:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return questions

# CheckLog


@app_v1.get("/check-logs/", tags=["CheckLog"], response_model=List[schemas.CheckLog])
def read_vehicle(db: Session = Depends(get_db)):
    check_logs = crud.get_checklogs(db)
    if check_logs is None:
        raise HTTPException(status_code=404, detail="Check logs not found")
    return check_logs


@app_v1.get("/check-log/{checklog_id}", tags=["CheckLog"], response_model=schemas.CheckLog)
def read_checklog(checklog_id: int, db: Session = Depends(get_db)):
    checklog = crud.get_checklog(db, checklog_id=checklog_id)
    if checklog is None:
        raise HTTPException(status_code=404, detail="Check log not found!")
    return checklog


@app_v1.post("/check-log/", tags=["CheckLog"], response_model=schemas.CheckLog, status_code=201)
def write_check_log(*, db: Session = Depends(get_db), payload: schemas.CheckLog):
    return crud.create_check_log(db, payload=payload)


@app_v1.delete("/check-log/{checklog_id}", tags=["CheckLog"], response_model=schemas.CheckLog)
def delete_vehicle(checklog_id: int, db: Session = Depends(get_db)):
    vehicle = crud.get_checklog(db, checklog_id=checklog_id)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Checklog not found")
    vehicle = crud.delete_checklog(db, checklog_id=checklog_id)
    return vehicle


# Answer

@app_v1.get("/answers/", tags=["Answer"], response_model=List[schemas.Answer])
def get_answers(db: Session = Depends(get_db)):
    answers = crud.get_answers(db)
    return answers


@app_v1.post("/answer/", tags=["Answer"], response_model=schemas.Answer, status_code=201)
def write_answer(*, db: Session = Depends(get_db), payload: schemas.Answer):
    return crud.create_answer(db, payload=payload)


@app_v1.delete("/answers/{answer_id}", tags=["Answer"], response_model=schemas.Answer)
def delete_vehicle(answer_id: int, db: Session = Depends(get_db)):
    answer = crud.get_answer(db, answer_id=answer_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    answer = crud.delete_answer(db, answer_id=answer_id)
    return answer
