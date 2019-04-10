from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from map.models import Car
from map.forms import CarForm

def home(request):
	# Get all car objects from db
	cars = Car.objects.all().filter(available=True)
	args = {'cars': cars }
	# if request.method == "POST":
	# 	car_number_plate = request.POST.get('number_plate_id', None) # Set number_plate value
	# 	set_car = Car.objects.get(number_plate=car_number_plate) # Set Car
	# 	# set_car.available = False # Change available to False
	# 	set_car.save()
	# 	redirect('map/confirmation.html')
	# else:
		# Argument to contain list of our car model

	return render(request, 'map/homepage.html', args)

def get_mylocation(request):
    if request.GET.get('find-me'):
        longitude = request.COOKIES.get('longitude', '')
        latitude = request.COOKIES.get('latdyitude', '')
    return render(request, 'map/homepage.html',
                {'longitude' :longitude,
                 'latitude' :latitude})

def car_detail_view(request, id):
	if request.method == "POST":
		form = CarForm(request.POST)
		print(form.is_valid())
		if form.is_valid():
			car_save = form.instance
			get_car = Car.objects.get(number_plate=car_save.number_plate)
			get_car.available = False
			get_car.save()
			return redirect('/')
		else:
			print(form.errors)
	else:
		car = Car.objects.get(id=id)
		form = CarForm()
		form.fields['brand'].initial = car.brand
		form.fields['number_plate'].initial = car.number_plate
		form.fields['price'].initial = car.price
		form.fields['available'].initial = car.available
		args = {
			'car':car,
			'form':form
		}
	return render(request, 'map/confirmation.html', args)
