# import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sql_app.routes.v1 import app_v1
from starlette.requests import Request
from starlette.responses import Response
from starlette.status import HTTP_401_UNAUTHORIZED
from sql_app.utils.security import check_jwt_token
from datetime import datetime

app = FastAPI(
    title="Vehicle Inspection API Documentation",
    description="To come...",
    version="0.0.1"
)

app.mount("/v1", app_v1)


@app.middleware("http")
async def middleware(request: Request, call_next):
    start_time = datetime.utcnow()
    # modify request
    if not any(word in str(request.url) for word in ["/token", "/docs", "/openapi.json"]):
        try:
            jwt_token = request.headers["Authorization"].split("Bearer ")[1]
            is_valid = check_jwt_token(jwt_token)
        except Exception as e:
            is_valid = False

        if not is_valid:
            return Response("Unathorized", status_code=HTTP_401_UNAUTHORIZED)

    response = await call_next(request)
    # modify response
    #execution_time = (datetime.utcnow() - start_time).microseconds
    #response.headers["x-execution-time"] = str(execution_time)
    return response
