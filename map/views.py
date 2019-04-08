from django.shortcuts import render
from django.http import HttpResponse
from map.models import Car
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'map/homepage.html'
    
    def home(request):
        # Get all car objects from db
        cars = Car.objects.filter(available=True)

        # Argument to contain list of our car model
        args = {'cars': cars}
        return render(request, self.template_name, args)

# def get_mylocation(request):
#     if request.GET.get('find-me'):
#         longitude = request.COOKIES.get('longitude', '')
#         latitude = request.COOKIES.get('latitude', '')
#     return render(request, 'map/homepage.html',
#                 {'longitude' :longitude,
#                  'latitude' :latitude})
