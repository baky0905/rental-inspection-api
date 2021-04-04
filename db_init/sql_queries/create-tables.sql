CREATE TABLE "vehicle" (
  "id" SERIAL PRIMARY KEY,
  "make" VARCHAR,
  "num_of_doors" INT,
  "horsepower" INT,
  "image_url" VARCHAR,
  "created_at" TIMESTAMP,
  "updated_at" TIMESTAMP DEFAULT (now()),
  "category" INT
);
CREATE TABLE "signature" (
  "id" SERIAL PRIMARY KEY,
  "signature" VARCHAR,
  "num_of_doors" INT,
  "created_at" TIMESTAMP,
  "updated_at" TIMESTAMP DEFAULT (now())
);
CREATE TABLE "category" (
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR,
  "created_at" TIMESTAMP,
  "updated_at" TIMESTAMP DEFAULT (now())
);
CREATE TABLE "category_question" (
  "id" SERIAL PRIMARY KEY,
  "category" INT,
  "question" INT
);
CREATE TABLE "answer" (
  "id" INT PRIMARY KEY,
  "answer" VARCHAR,
  "created_at" TIMESTAMP,
  "updated_at" TIMESTAMP DEFAULT (now()),
  "comment" VARCHAR,
  "photo_url" VARCHAR,
  "question" INT,
  "check_log" INT
);
CREATE TABLE "question" (
  "id" INT PRIMARY KEY,
  "question" VARCHAR,
  "frequency_check" VARCHAR,
  "created_at" TIMESTAMP,
  "updated_at" TIMESTAMP DEFAULT (now())
);
CREATE TABLE "check_log" (
  "id" SERIAL PRIMARY KEY,
  "comment" VARCHAR,
  "created_at" TIMESTAMP,
  "updated_at" TIMESTAMP DEFAULT (now()),
  "driver" INT,
  "vehicle" INT,
  "signature" INT
);
CREATE TABLE "driver" (
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR,
  "phone_number" INT,
  "email" VARCHAR,
  "username" VARCHAR,
  "password" VARCHAR,
  "created_at" TIMESTAMP,
  "updated_at" TIMESTAMP DEFAULT (now())
);
CREATE TABLE "user" (
  "id" INT PRIMARY KEY,
  "username" VARCHAR,
  "password" VARCHAR,
  "role" VARCHAR,
  "created_at" TIMESTAMP,
  "updated_at" TIMESTAMP DEFAULT (now())
);
ALTER TABLE "category_question"
ADD FOREIGN KEY ("category") REFERENCES "category" ("id");
ALTER TABLE "vehicle"
ADD FOREIGN KEY ("category") REFERENCES "category" ("id");
ALTER TABLE "check_log"
ADD FOREIGN KEY ("driver") REFERENCES "driver" ("id");
ALTER TABLE "check_log"
ADD FOREIGN KEY ("vehicle") REFERENCES "vehicle" ("id");
ALTER TABLE "check_log"
ADD FOREIGN KEY ("signature") REFERENCES "signature" ("id");
ALTER TABLE "answer"
ADD FOREIGN KEY ("check_log") REFERENCES "check_log" ("id");
ALTER TABLE "category_question"
ADD FOREIGN KEY ("question") REFERENCES "question" ("id");