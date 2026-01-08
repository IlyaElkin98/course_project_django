from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from message.models import Message


class MessageCreateView(CreateView):
    model = Message
    fields = ['topic_letter', 'body_letter']
    template_name = 'message/message_form.html'
    success_url = reverse_lazy('message:messages')


class MessageListView(ListView):
    model = Message
    template_name = 'message/message_list.html'
    context_object_name = 'messages'


class MessageUpdateView(UpdateView):
    model = Message
    fields = ['topic_letter', 'body_letter']

    def get_success_url(self):
        return reverse('message:detail_message', kwargs={'pk': self.object.pk})


class MessageDetailView(DetailView):
    model = Message
    template_name = 'message/detail_message.html'
    context_object_name = 'message'


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'message/confirm_delete_message.html'
    success_url = reverse_lazy('message:messages_list')