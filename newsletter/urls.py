from django.urls import path
from .views import (
    NewsletterCreateView,
    NewsletterDeleteView,
    NewsletterDetailView,
    NewsletterUpdateView,
    NewsletterListCreate, send_newsletter,
)
from newsletter.apps import NewsletterConfig

app_name = NewsletterConfig.name

urlpatterns = [
    path("new/", NewsletterCreateView.as_view(), name="create_newsletter"),
    path("newsletters/", NewsletterListCreate.as_view(), name="newsletters_list"),
    path("detail_newsletter/<int:pk>/", NewsletterDetailView.as_view(), name="detail_newsletter"),
    path("detail_newsletter/<int:pk>/update/", NewsletterUpdateView.as_view(), name="update_newsletter"),
    path("delete_newsletter/<int:pk>/", NewsletterDeleteView.as_view(), name="delete_newsletter"),
    path("send_newsletter/<int:pk>/", send_newsletter, name="send_newsletter"),
]
