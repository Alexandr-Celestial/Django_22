from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from users.apps import UsersConfig
from users.views import validation_user, CreateUserView

app_name=UsersConfig.name

urlpatterns = [
    path('create_user/', CreateUserView.as_view(), name='create_user'),
    path('login/', LoginView.as_view(template_name='login_user.html'), name='login'),
    path('valid_token/<str:token>', validation_user, name='valid_token'),
    path('logout/', LogoutView.as_view(), name='logout'),
]