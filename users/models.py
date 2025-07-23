from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    username = None
    email =models.EmailField(verbose_name='email', unique=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='avatar/', verbose_name='Аватар')
    phone_number = models.CharField(max_length=15, null=True, blank=True, verbose_name='Номер телефона')
    country = models.CharField(max_length=100, null=True, blank=True, verbose_name='Страна')
    token = models.CharField(max_length=100, null=True, blank=True, verbose_name='Токен')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.email