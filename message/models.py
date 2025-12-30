from django.db import models

class Message(models.Model):
    topic_letter = models.CharField(
        verbose_name='Тема письма',
        help_text='Введите тему письма'
    )

    body_letter = models.TextField(
        verbose_name='Тело письма',
        help_text='Содержание письма'
    )

