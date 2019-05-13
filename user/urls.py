from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import UserDashPage, RegisterPageView, UserDashPage, LoginPageView

urlpatterns = [
    path('register/', RegisterPageView.as_view(), name='register'),
    path('login/', LoginPageView.as_view(template_name='user/login.html'), name='login'),
    path('user', UserDashPage.as_view(), name='user'),
    # path('history', BookingHistoryPage.as_view(), name='history'),
]
