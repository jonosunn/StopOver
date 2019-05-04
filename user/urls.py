from django.urls import path
from . import views
from .views import RegisterPageView

urlpatterns = [
    path('register/', RegisterPageView.as.view(), name='register'),
]
