from django.shortcuts import render, get_object_or_404
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

    def get(self, request, pk):
        newsletter = get_object_or_404(Newsletter, pk=pk)
        newsletter.update_status()
        return render(request, 'newsletter/detail_newsletter.html', {'newsletter': newsletter})


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    form_class = NewsletterForm


    def get_success_url(self):
        return reverse("newsletter:detail_newsletter", kwargs={"pk": self.object.pk})


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    template_name = "newsletter/confirm_delete_newsletter.html"
    success_url = reverse_lazy("newsletter:newsletters_list")

