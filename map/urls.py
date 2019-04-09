from django.urls import path
from . import views
from .views import HomePageView, CarListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('', CarListView.as_view(), name='carlist'),
    # path('', views.HomePageView.home),
    # path('', views.get_mylocation),
]
