from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from mail_recipient.models import Recipient

class RecipientCreateView(CreateView):
    model = Recipient
    fields = ['email', 'full_name', 'comment']
    template_name = 'recipient/recipient_form.html'
    success_url = reverse_lazy('recipient:recipients')


class RecipientListView(ListView):
    model = Recipient
    template_name = 'recipient/recipient_list.html'
    context_object_name = 'recipients'


class RecipientDetailView(DetailView):
    model = Recipient
    template_name = 'recipient/recipient_detail.html'
    context_object_name = 'recipient'


class RecipientUpdateView(UpdateView):
    model = Recipient
    fields = ['email', 'full_name', 'comment']

    def get_success_url(self):
        return reverse('recipient:recipient_detail', kwargs={'pk' : self.object.pk})


class RecipientDeleteView(DeleteView):
    model = Recipient
    template_name = 'recipient/recipient_confirm_delete.html'
    success_url = reverse_lazy('recipient:recipients')








