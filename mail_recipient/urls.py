from django.conf import settings
from django.urls import path
from .views import (
    RecipientCreateView,
    RecipientListView,
    RecipientDeleteView,
    RecipientUpdateView,
    RecipientDetailView,
)
from mail_recipient.apps import MailRecipientConfig

app_name = MailRecipientConfig.name

urlpatterns = [
    path("new/", RecipientCreateView.as_view(), name="create_recipient"),
    path("recipients/", RecipientListView.as_view(), name="recipients_list"),
    path(
        "detail_recipient/<int:pk>/",
        RecipientDetailView.as_view(),
        name="detail_recipient",
    ),
    path(
        "detail_recipient/<int:pk>/update/",
        RecipientUpdateView.as_view(),
        name="update_recipient",
    ),
    path(
        "delete_recipient/<int:pk>/",
        RecipientDeleteView.as_view(),
        name="delete_recipient",
    ),
]
