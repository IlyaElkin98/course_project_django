from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("recipient/", include(("mail_recipient.urls", "mail_recipient"), namespace="mail_recipient")),
    path("message/", include(("message.urls", "message"), namespace="message")),
    path("newsletter/", include(("newsletter.urls", "newsletter"), namespace="newsletter")),
    path("", include(('message.urls', 'main'), namespace='main'))
]
