from django.urls import path
from . import views
from .views import ConfirmationPage, BookingPage
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('booking/<slug:number_plate>', BookingPage.as_view(), name='booking'),
    path('confirmation/', ConfirmationPage.as_view(), name='confirmation'),
]
