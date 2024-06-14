from ninja import Router
from django.contrib.auth import authenticate
from django.contrib.auth.models import User as DjangoUser
from ninja.errors import HttpError
from ninja_jwt.tokens import RefreshToken

from backend.apps.account.auth.auth import BearerAuth
from backend.apps.account.schemas import UserSchemas
from backend.apps.account.models import UserProfile


router = Router()

auth = BearerAuth()

@router.post("/token")
def token(request, username: str, password: str):
    user = authenticate(request, username=username, password=password)
    if user is None:
        raise HttpError(401, "Не правильный username or password")

    # Создаем JWT токены
    refresh = RefreshToken.for_user(user)
    return {"access_token": str(refresh.access_token), "refresh_token": str(refresh)}

@router.get("/user", auth=auth, response=UserSchemas)
def get_current_user(request):
    user = request.auth
    try:
        user_profile = UserProfile.objects.get(user=user)
        return {
            "id": user_profile.id,
            "username": user.username,
            "first_name": user_profile.first_name,
            "last_name": user_profile.last_name,
            "photo": user_profile.photo.url if user_profile.photo else None
        }
    except UserProfile.DoesNotExist:
        raise HttpError(404, "Профиль пользователя не найден")

def protected_route(request):
    return {"message": "This is a protected route", "user": request.auth.username}