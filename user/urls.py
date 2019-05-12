from django.urls import path
from . import views
from .views import UserDashPage, BookingHistoryPage
# from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('user', UserDashPage.as_view(), name='user'),
    path('history', BookingHistoryPage.as_view(), name='history'),
]
