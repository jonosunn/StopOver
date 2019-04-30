from django.shortcuts import render, redirect
from django.http import HttpResponse
from map.models import Car
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse


from map.forms import CarForm

class HomePageView(TemplateView):
	template_name = 'map/homepage.html'

	def get_context_data(self, *args, **kwargs):
		print("get_context_data")
		numberplate = self.request.GET.get("number_plate")	# Remove later
		if numberplate != None:
			set_car = Car.objects.get(number_plate=numberplate)
		context = super(HomePageView, self).get_context_data(*args, **kwargs)
		context['cars'] = Car.objects.filter(available=True)
		return context
	# Reciving ajax request for session timer
	def post(self, request):
		if request.method == "POST":
			number_plate = request.POST['car'] # set data from POST into number_plate variable
			set_car = Car.objects.get(number_plate=number_plate) # set car object with the car that has number_plate
			set_car.available = True	# change set_car available to True
			set_car.save()	# save changes into the database
		return render(request, self.template_name)

class ConfirmationPage(TemplateView):
	template_name = 'confirmation/confirmation.html'

	# Recieving get request from form
	def get(self, request, number_plate):
		print("GET METHOD")
		print("number_plate: ", number_plate)
		host = request.get_host();

		set_car = Car.objects.get(number_plate=number_plate)

		paypal_dict = {
	        'business': settings.PAYPAL_RECEIVER_EMAIL,
	        'amount': str(set_car.price),
	        'item_name': 'Order {}'.format(set_car.number_plate),
	        'invoice': str(set_car.id),
	        'currency_code': 'AUD',
	        'return_url': 'http://{}{}'.format(host,
	                                           reverse('payment_done')),
	    }

		form = PayPalPaymentsForm(initial=paypal_dict)
		set_car = Car.objects.get(number_plate=number_plate) # Set car object using the number_plate
		set_car.available = False	# Set the selected car to false so other users can't select the car
		set_car.save() # Save car object to database

		args = {
        	"car": set_car,
        	"form": form
    	}
		return render(request, self.template_name, args)


class SuccessPage(TemplateView):
	template_name = 'confirmation/paysuccess.html'
	#TODO: SET CORRECT URLS
	@csrf_exempt
	def get_context_data(self, *args, **kwargs):
		context = super(SuccessPage, self).get_context_data(*args, **kwargs)
		context['cars'] = Car.objects.filter(available=True)
		return context
