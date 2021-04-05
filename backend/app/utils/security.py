import time
import os
import jwt
from app import schemas
from datetime import datetime, timedelta
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from starlette.status import HTTP_401_UNAUTHORIZED
load_dotenv(dotenv_path=".env")


JWT_EXPIRATION_TIME_MINUTES = int(os.getenv("JWT_EXPIRATION_TIME_MINUTES"))
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

password_context = CryptContext(schemes=["bcrypt"])
oauth_schema = OAuth2PasswordBearer(tokenUrl="token")


jwt_user_1 = {
    "username": "kbaka",
    "password": "$2b$12$dtVWAX7AEnAmFlvNIiP7J.6RaZYk5NO3KXEmJk2HZdmpyz549e3um",
    "disabled": False,
    "role": "admin"
}

fake_jwt_user_1 = schemas.JWTUser(**jwt_user_1)


def get_hashed_password(password):
    return password_context.hash(password)


def verify_password(plain_password, hashed_password):
    try:
        return password_context.verify(plain_password, hashed_password)
    except Exception as e:
        print(e)
        return False

# Authenticate username and password to give JWT token


def authenticate_user(user: schemas.JWTUser):
    if fake_jwt_user_1.username == user.username:
        if verify_password(user.password, fake_jwt_user_1.password):
            user.role = "admin"
            return user

    return None

# Create access JWT token


def create_jwt_token(user: schemas.JWTUser):

    expiration = datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_TIME_MINUTES)

    jwt_payload = {
        "sub": user.username,
        "role": user.role,
        "exp": expiration
    }

    jwt_token = jwt.encode(jwt_payload, JWT_SECRET_KEY,
                           algorithm=JWT_ALGORITHM)

    return jwt_token

# Check if JWT token is correct


def check_jwt_token(token: str = Depends(oauth_schema)):
    try:
        jwt_payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=JWT_ALGORITHM)
        username = jwt_payload.get("sub")
        role = jwt_payload.get("role")
        expiration = jwt_payload.get("exp")

        if time.time() < expiration:
            if fake_jwt_user_1.username == username:
                return final_checks(role)

    except Exception as e:
        return False

    return False
    # Last checking and returning the final result


def final_checks(role: str):
    if role == "admin":
        return True
    else:
        return False
