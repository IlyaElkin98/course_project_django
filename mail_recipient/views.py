from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from mail_recipient.models import Recipient

class RecipientCreateView(CreateView):
    model = Recipient
    fields = ['email', 'full_name', 'comment']
    template_name = 'mail_recipient/message_form.html'
    success_url = reverse_lazy('mail_recipient:recipients_list')


class RecipientListView(ListView):
    model = Recipient
    template_name = 'mail_recipient/recipients_list.html'
    context_object_name = 'recipients'


class RecipientDetailView(DetailView):
    model = Recipient
    template_name = 'mail_recipient/detail_message.html'
    context_object_name = 'recipient'


class RecipientUpdateView(UpdateView):
    model = Recipient
    fields = ['email', 'full_name', 'comment']

    def get_success_url(self):
        return reverse('mail_recipient:detail_recipient', kwargs={'pk' : self.object.pk})


class RecipientDeleteView(DeleteView):
    model = Recipient
    template_name = 'mail_recipient/confirm_delete_message.html'
    success_url = reverse_lazy('mail_recipient:recipients_list')








