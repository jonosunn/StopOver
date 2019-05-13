from django.urls import path
from . import views
from .views import HomePageView, SimulationPageView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('admin/car/simulation', SimulationPageView.as_view(), name='simulation')
]

