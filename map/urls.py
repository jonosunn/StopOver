from django.urls import path
from . import views
from .views import HomePageView, SimulationPageView
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('admin/car/simulation', staff_member_required(SimulationPageView.as_view()), name='simulation')
]
