from django.urls import path
from django.conf import settings

from .views import LoginView


urlpatterns = [
    path(settings.LOGIN_URL, LoginView.as_view(), name='login'),
]
