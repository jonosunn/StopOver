from django.urls import path
from . import views
from .views import ConfirmationPage, BookingPage
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('booking/<slug:number_plate>', ConfirmationPage.as_view(), name='booking'),
    path('confirmation/', SuccessPage.as_view(), name='confirmation'),
]
