import jwt
from jwt import PyJWTError
from asgiref.sync import sync_to_async
from django.http import HttpRequest
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from ninja.security import HttpBearer

from backend.config import settings
from backend.apps.account.auth.schemas import TokenPayload

def create_access_token(*, data: dict, expires_delta: timedelta = None):
    """Создание токена"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire, "sub": settings.access_token_jwt_subject})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def create_token(user_id: int):
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": create_access_token(
            data={"user_id": user_id}, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


def get_current_user(token: str):
    """Проверка аутентифицированного пользователя"""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except PyJWTError:
        return None
    user_model = get_user_model()
    user = get_object_or_404(user_model, id=token_data.user_id)
    return user


class AuthBearer(HttpBearer):
    async def authenticate(self, request: HttpRequest, token: str):
        user = await sync_to_async(get_current_user)(token)
        if user:
            return user
