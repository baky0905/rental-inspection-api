from typing import List

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


@app.get("/vehicles/", response_model=List[schemas.Vehicle])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_vehicles(db, skip=skip, limit=limit)
    return items


@app.get("/vehicles/{vehicle_id}", response_model=schemas.Vehicle)
def read_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    vehicle = crud.get_vehicle(db, vehicle_id=vehicle_id)
    if vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle


@app.delete("/vehicles/{vehicle_id}", response_model=schemas.Vehicle)
def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    vehicle = crud.get_vehicle(db, vehicle_id=vehicle_id)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    vehicle = crud.delete_vehicle(db, vehicle_id=vehicle_id)
    return vehicle  # f"successfuly removed vehicle by id: {vehicle_id}"


@app.post("/vehicle/", response_model=schemas.Vehicle, status_code=201)
def write_vehicle(*, db: Session = Depends(get_db), payload: schemas.Vehicle):
    return crud.create_vehicle(db, payload=payload)


@app.get("/questions/{vehicle_id}", response_model=List[schemas.Question])
def read_questions(vehicle_id: int, db: Session = Depends(get_db)):
    questions = crud.get_questions_by_vehicle_id(db, vehicle_id=vehicle_id)
    if len(questions) == 0:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return questions


@app.get("/check-logs/", response_model=List[schemas.CheckLog])
def read_vehicle(db: Session = Depends(get_db)):
    check_logs = crud.get_checklogs(db)
    if check_logs is None:
        raise HTTPException(status_code=404, detail="Check logs not found")
    return check_logs


@app.post("/check-log/", response_model=List[schemas.CheckLog])
def write_check_log(db: Session = Depends((get_db))):
    check_log_item = crud.create_check_log(db)
    return check_log_item


# @app.post("/vehicles/", response_model=schemas.User)
# def read_users(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)
# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users
# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)
# @app.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items
#
