from django.urls import path
from . import views
from .views import UserDashPage
# from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('user', UserDashPage.as_view(), name='user'),
]
