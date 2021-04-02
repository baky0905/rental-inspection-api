from typing import List
# import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Vehicle


@app.get("/vehicles/", response_model=List[schemas.Vehicle])
def read_items(db: Session = Depends(get_db)):
    items = crud.get_vehicles(db)
    return items


@app.get("/vehicles/{vehicle_id}", response_model=schemas.Vehicle)
def read_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    vehicle = crud.get_vehicle(db, vehicle_id=vehicle_id)
    if vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle


@app.post("/vehicle/", response_model=schemas.Vehicle, status_code=201)
def write_vehicle(*, db: Session = Depends(get_db), payload: schemas.Vehicle):
    return crud.create_vehicle(db, payload=payload)


@app.delete("/vehicles/{vehicle_id}", response_model=schemas.Vehicle)
def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    vehicle = crud.get_vehicle(db, vehicle_id=vehicle_id)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    vehicle = crud.delete_vehicle(db, vehicle_id=vehicle_id)
    return vehicle  # f"successfuly removed vehicle by id: {vehicle_id}"


# Question


@app.get("/questions/{vehicle_id}", response_model=List[schemas.Question])
def read_questions(vehicle_id: int, db: Session = Depends(get_db)):
    questions = crud.get_questions_by_vehicle_id(db, vehicle_id=vehicle_id)
    if len(questions) == 0:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return questions

# CheckLog


@app.get("/check-logs/", response_model=List[schemas.CheckLog])
def read_vehicle(db: Session = Depends(get_db)):
    check_logs = crud.get_checklogs(db)
    if check_logs is None:
        raise HTTPException(status_code=404, detail="Check logs not found")
    return check_logs


@app.get("/check-logs/{checklog_id}", response_model=schemas.CheckLog)
def read_checklog(checklog_id: int, db: Session = Depends(get_db)):
    checklog = crud.get_checklog(db, checklog_id=checklog_id)
    if checklog is None:
        raise HTTPException(status_code=404, detail="Check log not found!")
    return checklog


@app.post("/check-log/", response_model=schemas.CheckLog, status_code=201)
def write_check_log(*, db: Session = Depends(get_db), payload: schemas.CheckLog):
    return crud.create_check_log(db, payload=payload)


@app.delete("/check-logs/{checklog_id}", response_model=schemas.CheckLog)
def delete_vehicle(checklog_id: int, db: Session = Depends(get_db)):
    vehicle = crud.get_checklog(db, checklog_id=checklog_id)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Checklog not found")
    vehicle = crud.delete_checklog(db, checklog_id=checklog_id)
    return vehicle  # f"successfuly removed vehicle by id: {vehicle_id}"


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
