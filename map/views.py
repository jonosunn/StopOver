from django.shortcuts import render
from django.http import HttpResponse
from map.models import Car

def home(request):
	# Get all car objects from db
	cars = Car.objects.all()

	# Argument to contain list of our car model
	args = {'cars': cars}
	return render(request, 'map/homepage.html', args)
