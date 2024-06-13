from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField('Имя', max_length=599, blank=True)
    last_name = models.CharField('Фамилия', max_length=599, blank=True)
    photo = models.ImageField('Пользователи', upload_to='user_photos/', blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Пользователя'
