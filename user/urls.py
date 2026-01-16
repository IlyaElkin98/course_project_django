from . import views
from .views import custom_logout
from django.contrib.auth.views import LoginView
from django.urls import path, include
from user.apps import UserConfig
from user.views import UserCreateView, email_varification
from django.contrib.auth import views as auth_views

app_name = UserConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_varification, name='email-confirm'),

    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', views.CustomUserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='custom_registration/password_reset_complete.html'), name='password_reset_complete'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='custom_registration/password_reset_done.html'), name='password_reset_done'),
]