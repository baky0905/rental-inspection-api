FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7


COPY ./sql_app /app
COPY ./requirements.txt /app

RUN pip install -r requirements.txt