from django.urls import path
from .views import NewsletterCreateView, NewsletterDeleteView, NewsletterDetailView, NewsletterUpdateView, NewsletterListCreate
from mail_recipient.apps import MailRecipientConfig

app_name = MailRecipientConfig.name

urlpatterns = [
    path('new/', NewsletterCreateView.as_view(), name='create_recipient'),
    path('newsletters/', NewsletterListCreate.as_view(), name='recipients_list'),
    path('detail_newsletter/<int:pk>/', NewsletterDetailView.as_view(), name='detail_newsletter'),
    path('detail_newsletter/<int:pk>/update/', NewsletterUpdateView.as_view(), name='update_newsletter'),
    path('delete_newsletter/<int:pk>/', NewsletterDeleteView.as_view(), name='delete_newsletter')
]