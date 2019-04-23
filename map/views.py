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
		numberplate = self.request.GET.get("number_plate")
		if numberplate != None:
			set_car = Car.objects.get(number_plate=numberplate)
		context = super(HomePageView, self).get_context_data(*args, **kwargs)
		context['cars'] = Car.objects.filter(available=True)
		return context

class ConfirmationPage(TemplateView):
	template_name = 'confirmation/confirmation.html'

	def get(self, request, number_plate):
		print("GET METHOD")
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
		args = {
        	"car": set_car,
        	"form": form
    	}
		
		
		return render(request, self.template_name, args)
	
	#TODO: SET CORRECT URLS
	@csrf_exempt
	def payment_done(request):
	    return render(request, 'confirmation/paysuccess.html')
	
