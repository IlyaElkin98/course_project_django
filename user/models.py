from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    avatar = models.ImageField(upload_to="media/user", width_field=150, height_field=150, verbose_name="Аватар", help_text="Загрузите аватар", null=True, blank=True)
    phone_number = models.CharField(blank=True, help_text="Укажите номер телефона", null=True)
    country = models.CharField(max_length=50, verbose_name="Страна", help_text="Укажите страну", blank=True, null=True)
    token = models.CharField(max_length=100, verbose_name='Token', blank=True, null=True)



    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()  # Устанавливаем менеджер пользователей

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.email

