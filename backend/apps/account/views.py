import uuid
import os

from typing import List
from ninja import Router, File
from ninja.files import UploadedFile
from django.contrib.auth import authenticate
from django.contrib.auth.models import User as DjangoUser
from ninja.errors import HttpError
from ninja_jwt.tokens import RefreshToken

from backend.apps.account.auth.auth import auth
from backend.apps.account.schemas import UserSchemas
from backend.apps.account.models import UserProfile
from backend.apps.account.utils import verify_face
from backend.config import settings

router = Router()

@router.post("/api/token")
def token(request, username: str, password: str):
    user = authenticate(request, username=username, password=password)
    if user is None:
        raise HttpError(401, "Invalid username or password")

    # Создаем JWT токены
    refresh = RefreshToken.for_user(user)
    return {"access_token": str(refresh.access_token), "refresh_token": str(refresh)}

@router.get("/api/current-user", auth=auth, response=UserSchemas)
def get_current_user(request):
    user = request.auth
    user_profile = UserProfile.objects.get(user=user)
    return {
        "id": user_profile.id,
        "username": user.username,
        "first_name": user_profile.first_name,
        "last_name": user_profile.last_name,
        "photo": user_profile.photo.url if user_profile.photo else None
    }


@router.post("/api/face-login", response={200: dict, 401: str})
def face_login(request, file: UploadedFile):
    temp_dir = os.path.join(settings.MEDIA_ROOT, 'temporary_photos')
    os.makedirs(temp_dir, exist_ok=True)

    unique_filename = f"{uuid.uuid4()}.jpg"
    file_path = os.path.join(temp_dir, unique_filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    result = verify_face(file_path)

    os.remove(file_path)

    if result == "Unknown":
        return 401, "Доступ запрещён"
    else:
        try:
            user = UserProfile.objects.get(user__username=result).user
            refresh = RefreshToken.for_user(user)
            return {
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh)
            }
        except UserProfile.DoesNotExist:
            return 401, "Доступ запрещён"