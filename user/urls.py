from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import RegisterPageView

urlpatterns = [
    path('register/', RegisterPageView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
]
