from django.urls import path
from . import views
from .views import HomePageView

urlpatterns = [
<<<<<<< HEAD
    path('', views.home, name='map-home'),
    path('', views.get_mylocation),
    path('confirmation/<int:id>', views.car_detail_view, name='confirmation'),
=======
    path('', HomePageView.as_view(), name='home'),
>>>>>>> 287a1a25a4a24c306feaeb4b34c81e4b13cb5ac4
]
