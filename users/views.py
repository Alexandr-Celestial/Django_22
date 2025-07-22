import os
import secrets
from gc import get_objects

from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from parso.python.tree import Class

from config.settings import EMAIL_HOST_USER
from users.models import CustomUser


# Create your views here.

def validation_user(requests, token):
    user: CustomUser = get_object_or_404(CustomUser, token=token)
    if not user: return PermissionDenied
    user.is_active = True
    user.is_staff = True
    user.save()
    return redirect('catalog:home')

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)

class CreateUserView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'user_create.html'
    success_url = reverse_lazy('catalog:home')

    # class Meta(UserCreationForm):
    #     model = CustomUser
    #     fields = '__all__'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.token = secrets.token_hex(16)
        user.save()

        url = f'http://{self.request.get_host()}/users/valid_token/{user.token}'
        print(url)
        send_mail('Предоставление доступа',
                  f'Пожалуйста перейдите на {url}',
                  EMAIL_HOST_USER,
                  [user.email])
        return super().form_valid(form)


