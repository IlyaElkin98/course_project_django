import os

from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from dotenv import load_dotenv

from mail_recipient.models import Recipient
from .forms import NewsletterForm
from .models import Newsletter
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib import messages

load_dotenv()


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


from django.shortcuts import get_object_or_404

def send_newsletter(request, pk):
    newsletter = get_object_or_404(Newsletter, pk=pk)
    if request.method == 'POST':
        form = NewsletterForm(request.POST, instance=newsletter)
        if form.is_valid():
            newsletter = form.save(commit=False)
            now = timezone.now()
            if newsletter.start_time <= now <= newsletter.end_time:
                recipients = Recipient.objects.filter(newsletters=newsletter)
                for recipient in recipients:
                    try:
                        send_mail(
                            newsletter.subject,
                            newsletter.content,
                            os.getenv('EMAIL'),
                            [recipient.email],
                            fail_silently=False,
                        )
                        messages.success(request, f"Письмо успешно отправлено {recipient.email}.")
                    except Exception as e:
                        messages.error(request, f"Ошибка отправки на {recipient.email}: {str(e)}.")
                return redirect('newsletter.views')
            else:
                messages.error(request, "Текущее время находится вне диапазона отправки.")
    else:
        form = NewsletterForm(instance=newsletter)
    return render(request, 'newsletter/send_newsletter.html', {'form': form, 'newsletter': newsletter})
