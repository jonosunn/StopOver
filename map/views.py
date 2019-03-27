from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'map/homepage.html')

def get_mylocation(request):
    if request.GET.get('find-me'):
        longitude = request.COOKIES.get('longitude', '')
        latitude = request.COOKIES.get('latitude', '')
    return render(request, 'map/homepage.html',
                {'longitude':longitude,
                 'latitude' :latitude})
