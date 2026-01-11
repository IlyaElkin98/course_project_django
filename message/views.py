from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from mail_recipient.models import Recipient
from message.forms import MessageForm
from message.models import Message
from newsletter.models import Newsletter


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = "message/message_form.html"
    success_url = reverse_lazy("message:messages_list")


class MessageListView(ListView):
    model = Message
    template_name = "message/message_list.html"
    context_object_name = "messages"


class MessageUpdateView(UpdateView):
    model = Message
    fields = ["topic_letter", "body_letter"]

    def get_success_url(self):
        return reverse("message:detail_message", kwargs={"pk": self.object.pk})


class MessageDetailView(DetailView):
    model = Message
    template_name = "message/detail_message.html"
    context_object_name = "message"


class MessageDeleteView(DeleteView):
    model = Message
    template_name = "message/confirm_delete_message.html"
    success_url = reverse_lazy("message:messages_list")

def main_page(request):
    # Общее количество всех созданных рассылок
    total_mailings = Newsletter.objects.count()

    # Количество активных рассылок
    active_mailings = Newsletter.objects.filter(
        status='Запущена'
    ).count()

    # Количество уникальных получателей
    unique_recipients = Recipient.objects.distinct().count()

    context = {
        'total_mailings': total_mailings,
        'active_mailings': active_mailings,
        'unique_recipients': unique_recipients,
    }

    return render(request, 'main_page.html', context)