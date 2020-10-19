from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from account.forms import UserCreateForm


class SignInView(SuccessMessageMixin, LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('news_site:start_page')
    success_message = 'Вход в систему выполнен успешно.'


class SignOutView(SuccessMessageMixin, LogoutView):
    success_url = reverse_lazy('news_site:start_page')
    success_message = 'Выход из системы выполнен успешно.'


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'account/registration.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('account:sign_in')
    success_message = 'Регистрация прошла успешно.'
