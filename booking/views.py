from django.shortcuts import render, redirect
from django.http import HttpResponse
from map.models import Car
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView
from django.conf import settings
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

class BookingPage(TemplateView):
	template_name = 'booking/booking.html'

	# Recieving get request from form
	def get(self, request, number_plate):
		set_car = Car.objects.get(number_plate=number_plate) # Set car object using the number_plate
		set_car.available = False	# Set the selected car to false so other users can't select the car
		set_car.save() # Save car object to database

		args = {
        	"car": set_car,
    	}
		return render(request, self.template_name, args)


class ConfirmationPage(TemplateView):
	template_name = 'confirmation/confirmation.html'
	#TODO: SET CORRECT URLS
	@csrf_exempt
	def get_context_data(self, *args, **kwargs):
		context = super(ConfirmationPage, self).get_context_data(*args, **kwargs)
		context['cars'] = Car.objects.filter(available=True)
		return context
