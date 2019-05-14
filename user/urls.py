from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views
from .views import UserDashPage, RegisterPageView, UserDashPage, LoginPageView

urlpatterns = [
    path('register/', RegisterPageView.as_view(), name='register'),
    path('login/', LoginPageView.as_view(template_name='user/login.html', redirect_authenticated_user=True), name='login'),
    path('user/', login_required(UserDashPage.as_view()), name='user'),
    path('accounts/', include('django.contrib.auth.urls')),

]
