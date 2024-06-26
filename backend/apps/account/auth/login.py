import logging
from ninja import Router
from ninja.errors import HttpError
from django.contrib.auth import authenticate, login

from backend.apps.account.schemas import LoginInput
from backend.apps.account.auth.jwt import create_token


router = Router()
logger = logging.getLogger(__name__)


@router.post("/login")
def login_user(request, data: LoginInput):
    # Аутентификация пользователя
    user = authenticate(request, username=data.username, password=data.password)

    if user is not None:
        # Логин пользователя в систему
        login(request, user)

        # Создание JWT токена
        token = create_token(user.id)

        # Возвращение данных пользователя и токена
        return {
            "message": "Вход выполнен успешно",
            "token": token,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name
        }
    else:
        logger.warning(f"Неудачная попытка входа для пользователя: {data.username}")

        # В случае неудачной аутентификации выбрасываем ошибку 401
        raise HttpError(401, "Неверные учетные данные")
