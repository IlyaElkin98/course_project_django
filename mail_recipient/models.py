from django.db import models

class Recipient(models.Model):
    email = models.CharField(
        verbose_name='Электронная почта',
        help_text='Введите электронную почту'
    )

    full_name = models.CharField(
        verbose_name="Ф.И.О.",
        help_text='Введите ФИО'
    )

    comment = models.TextField(
        verbose_name='Комментарий'
    )

