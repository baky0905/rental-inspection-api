# import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sql_app.routes.v1 import app_v1
from starlette.requests import Request
from starlette.responses import Response
from starlette.status import HTTP_401_UNAUTHORIZED
from sql_app.utils.security import check_jwt_token
from datetime import datetime
from sql_app.utils.security import authenticate_user, create_jwt_token, check_jwt_token
from sql_app import schemas
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Vehicle Inspection API Documentation",
    description="To come...",
    version="0.0.1"
)

app.include_router(app_v1,
                   prefix="/v1",
                   dependencies=[Depends(check_jwt_token)])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.post("/token", summary="It returns JWT Token.", tags=["Login"])
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):

    jwt_user_dict = {"username": form_data.username,
                     "password": form_data.password}
    jwt_user = schemas.JWTUser(**jwt_user_dict)
    user = authenticate_user(jwt_user)
    if user is None:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)

    jwt_token = create_jwt_token(user)
    return {"access_token": jwt_token, "token_type": 'Bearer'}


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
    execution_time = (datetime.utcnow() - start_time).microseconds
    response.headers["x-execution-time"] = str(execution_time)
    return response
