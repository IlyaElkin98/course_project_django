from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from .forms import NewsletterForm
from .models import Newsletter
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


class NewsletterCreateView(CreateView):
    model = Newsletter
    form_class = NewsletterForm
    template_name = "newsletter/newsletter_form.html"
    success_url = reverse_lazy("newsletter:newsletters_list")


class NewsletterListCreate(ListView):
    model = Newsletter
    template_name = "newsletter/newsletters_list.html"
    context_object_name = "newsletters"


class NewsletterDetailView(DetailView):
    model = Newsletter
    template_name = "newsletter/detail_newsletter.html"
    context_object_name = "newsletter"


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    fields = ["start_time", "end_time", "status", "messages", "recipients"]

    def get_success_url(self):
        return reverse("newsletter:detail_newsletter", kwargs={"pk": self.object.pk})


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    template_name = "newsletter/confirm_delete_newsletter.html"
    success_url = reverse_lazy("newsletter:newsletters_list")
