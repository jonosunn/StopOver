from django.urls import path
from . import views
from .views import HomePageView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]