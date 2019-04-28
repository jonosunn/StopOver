from django.urls import path
from . import views
from .views import HomePageView, ConfirmationPage, SuccessPage
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('confirmation/<slug:number_plate>', ConfirmationPage.as_view(), name='confirmation'),
#     path('confirmation/paysubmit', ConfirmationPage.as_view(), name='process_payment'),
    path('confirmation/paysuccess', SuccessPage.as_view(), name='payment_done'),
]
