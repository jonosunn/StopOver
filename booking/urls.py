from django.urls import path
from . import views
from .views import ConfirmationPage, BookingPage, SuccessPage
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('booking/<slug:number_plate>', login_required(BookingPage.as_view()), name='booking'),
    path('confirmation', login_required(ConfirmationPage.as_view()), name='confirmation'),
    path('success', login_required(SuccessPage.as_view()), name='success'),
]
