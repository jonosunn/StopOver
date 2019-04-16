from django.urls import path
from . import views
from .views import HomePageView, ConfirmationPage
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('confirmation/<slug:number_plate>', login_required(ConfirmationPage.as_view()), name='confirmation'),
]
