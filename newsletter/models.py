from django.db import models
from django.utils import timezone

from mail_recipient.models import Recipient
from message.models import Message


class Newsletter(models.Model):
    start_time = models.DateTimeField(verbose_name="Дата и время начало отправки")
    end_time = models.DateTimeField(verbose_name="Дата и время окончания отправки")
    status = models.CharField(max_length=20, default="Создана", verbose_name="Статус")
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, verbose_name="Сообщение"
    )
    recipients = models.ManyToManyField(Recipient, verbose_name="Получатели")

    def update_status(self):
        current_time = timezone.now

        if current_time < self.start_time:
            new_status = "Создана"
        elif self.start_time <= current_time <= self.end_time:
            new_status = "Запущена"
        else:
            new_status = "Завершена"

        if self.status != new_status:
            self.status = new_status
            self.save(update_fields=["status"])

    def __str__(self):
        return f"Рассылка {self.start_time} до {self.end_time} ({self.status})"
