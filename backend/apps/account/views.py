from ninja import Router
from django.contrib.auth import authenticate
from django.contrib.auth.models import User as DjangoUser
from ninja.errors import HttpError
from ninja_jwt.tokens import RefreshToken

from backend.apps.account.schemas import UserSchemas


router = Router()

@router.post("/token")
def token(request, username: str, password: str):
    user = authenticate(request, username=username, password=password)
    if user is None:
        raise HttpError(401, "Не правильный username or password")

    # Создаем JWT токены
    refresh = RefreshToken.for_user(user)
    return {"access_token": str(refresh.access_token), "refresh_token": str(refresh)}

@router.get("/user")
def get_all_user(request):
    users = DjangoUser.objects.all()
    return users
