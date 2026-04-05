from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from .forms import CustomUserCreationForm
from .models import CustomUser

from django.core.mail import send_mail
from django.contrib.auth import login


class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать на сайт нашего магазина'
        message = 'Спасибо, что зарегистрировались в нашем магазине!'
        from_email = 'kuprinasa@yandex.ru'
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)