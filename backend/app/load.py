from sqlalchemy import create_engine
from backend.app.database import SessionLocal, engine
from backend.app import models
import csv
import datetime
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")


db = SessionLocal()

models.Base.metadata.create_all(bind=engine)


SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")


#engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

# Base.metadata.create_all(engine)

db.query(models.Vehicle).filter(models.Vehicle.id == 1)

records = db.query(models.Vehicle).all()

vehicle = models.Vehicle
category = models.Category
category_question = models.CategoryQuestion
question = models.Question


records = (db.query(models.Question.question)
           .select_from(models.Question)
           .join(models.CategoryQuestion)
           .join(models.Category)
           .join(models.Vehicle)
           .filter(models.Vehicle.id == 1)
           .all()
           )

for v in records:
    print(v.make)

pd.DataFrame([record.__dict__ for record in records])

vehicle = models.Vehicle
category = models.Category
category_question = models.CategoryQuestion
question = models.Question

records = (db
           .query(vehicle, category)
           .join(category, category.id == vehicle.category)
           .all()
           )

records = (db
           .query(vehicle)
           .join(category, category.id == vehicle.category)
           .join(category_question, category.id == category_question.category)
           .join(question, category_question.question == question.id)
           .filter(vehicle.id == 1)
           )


pd.DataFrame([record.__dict__ for record in records]).columns
vehicle_id = 2
(db.query(models.Question.id, models.Question.question, models.Question.frequency_check)
 .select_from(models.Question)
 .join(models.CategoryQuestion)
 .join(models.Category)
 .join(models.Vehicle)
 .filter(models.Vehicle.id == vehicle_id)

 )


db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()

# with engine.connect() as con:
#     rs = con.execute(
#         '''SELECT v.make,
# c.name,
# q.question
# FROM vehicle v
# JOIN category c ON v.category = c.id
# JOIN category_question cq ON cq.category = c.id
# JOIN question q ON cq.question = q.id
# WHERE v.id = 1

#         ''')
#     data = rs.fetchall()
#     pd.DataFrame(data, columns=rs.keys())


# with open("sars_2003_complete_dataset_clean.csv", "r") as f:
#     csv_reader = csv.DictReader(f)

#     for row in csv_reader:
#         db_record = models.Record(
#             date=datetime.datetime.strptime(row["date"], "%Y-%m-%d"),
#             country=row["country"],
#             cases=row["cases"],
#             deaths=row["deaths"],
#             recoveries=row["recoveries"],
#         )
#         db.add(db_record)

#     db.commit()

# db.close()


"SELECT v.make, c.name, q.question FROM vehicle v JOIN category c ON v.category = c.id JOIN category_question cq ON cq.category = c.id JOIN question q ON cq.question = q.id WHERE v.id = 1"
