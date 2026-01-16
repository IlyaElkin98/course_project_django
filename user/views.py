import secrets
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from user.forms import UserRegisterForm
from user.models import User
from config.settings import EMAIL_HOST_USER
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from user.forms import CustomPasswordResetForm, CustomSetPasswordForm


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/user/email-confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f'Привет, перейди по ссылки для подтверждения регистрации {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)



def email_varification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('user:login'))


def custom_logout(request):
    logout(request)
    return redirect('main:main_page')


class CustomPasswordResetView(PasswordResetView):
    template_name = 'custom_registration/password_reset.html'
    email_template_name = 'custom_registration/password_reset_email.html'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('user:password_reset_done')


class CustomUserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'custom_registration/password_reset_confirm.html'
    success_url = reverse_lazy('user:password_reset_complete')
    form_class = CustomSetPasswordForm