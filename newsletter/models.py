from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from mail_recipient.models import Recipient
from message.models import Message


class Newsletter(models.Model):

    STATUS_CHOICES = [
        ('Создана', 'Создана'),
        ('Запущена', 'Запущена'),
        ('Завершена', 'Завершена'),
    ]

    start_time = models.DateTimeField(verbose_name="Дата и время начало отправки", default=timezone.now())
    end_time = models.DateTimeField(verbose_name="Дата и время окончания отправки")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name="Сообщение")
    recipients = models.ManyToManyField(Recipient, verbose_name="Получатели")

    def clean(self):
        if self.start_time < timezone.now():
            raise ValidationError("Дата начала рассылки не может быть в прошлом.")
        if self.start_time >= self.end_time:
            raise ValidationError("Дата начала рассылки должна быть раньше даты окончания.")

    def update_status(self):
        now = timezone.now()
        if now < self.start_time:
            new_status = 'Создана'
        elif self.start_time <= now <= self.end_time:
            new_status = 'Запущена'
        else:
            new_status = 'Завершена'

        if self.status != new_status:
            self.status = new_status
            self.save()

    def __str__(self):
        return f"Рассылка от {self.start_time} до {self.end_time} ({self.status})"
