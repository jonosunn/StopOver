from django.shortcuts import render, redirect
from django.http import HttpResponse
from map.models import Car
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt


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
		set_car = Car.objects.get(number_plate=number_plate)
		args = {
        	"car": set_car
    	}
		return render(request, self.template_name, args)
	
	#TODO: SET CORRECT URLS
	def process_payment(self):
		numberplate = self.request.GET.get("number_plate")
		if numberplate != None:
			set_car = Car.objects.get(number_plate=numberplate) 
			
		host = request.get_host();
		
		paypal_dict = {
	        'business': settings.PAYPAL_RECEIVER_EMAIL,
	        'amount': '%.2f' % set_car.price().quantize(
	            Decimal('.01')),
	        'item_name': 'Order {}'.format(set_car.id),
	        'invoice': str(numberplate),
	        'currency_code': 'AUD',
	        'return_url': 'http://{}{}'.format(host,
	                                           reverse('payment_done')),
	        'cancel_return': 'http://{}{}'.format(host,
	                                              reverse('payment_cancelled')),
	    }
		
		form = PayPalPaymentsForm(initial=paypal_dict)
		return render(request, 'confirmation/paysuccess.html', {'order': set_car, 'form': form})
	#TODO: SET CORRECT URLS
	@csrf_exempt
	def payment_done(request):
	    return render(request, 'confirmation/paysuccess.html')
	
