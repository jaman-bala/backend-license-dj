from ninja.security import HttpBearer
from ninja.errors import HttpError
from django.contrib.auth.models import User as DjangoUser
from ninja_jwt.tokens import RefreshToken

class BearerAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            refresh_token = RefreshToken(token)
            user_id = refresh_token.payload.get('user_id')
            user = DjangoUser.objects.get(id=user_id)
            return user
        except Exception as e:
            raise HttpError(401, "Вы ввели неверный ТОКЕН")
