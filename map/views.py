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

	def get_context_data(self, request):
		print("get_context_data")
		numberplate = self.request.GET.get("number_plate")
		if numberplate != None:
			set_car = Car.objects.get(number_plate=numberplate)
		context = super(HomePageView, self).get_context_data(*args, **kwargs)
		context['cars'] = Car.objects.filter(available=True)
		return context
	
	#TODO:
	def checkout(request):
		if request.method == 'POST':
			form = CheckoutForm(request.POST)
			if form.is_valid():
				cleaned_data = form.cleaned_data
	       #...
	       #...
		        cart.clear(request)
		        request.session['order_id'] = o.id
		        return redirect('process_payment')
		else:
			form = CheckoutForm()
	    	return (render(request, '', locals()))
        
	#TODO: SET CORRECT URLS
	def process_payment(self):
		numberplate = self.request.GET.get("number_plate")
		if numberplate != None:
			set_car = Car.objects.get(number_plate=numberplate) 
			
		paypal_dict = {
	        'business': settings.PAYPAL_RECEIVER_EMAIL,
	        'amount': '%.2f' % set_car.price().quantize(
	            Decimal('.01')),
	        'item_name': 'Order {}'.format(numberplate),
	        'invoice': str(numberplate),
	        'currency_code': 'AUD',
	        'notify_url': 'http://{}{}'.format(host,
	                                           reverse('paypal-ipn')),
	        'return_url': 'http://{}{}'.format(host,
	                                           reverse('payment_done')),
	        'cancel_return': 'http://{}{}'.format(host,
	                                              reverse('payment_cancelled')),
	    }
	 	form = PayPalPaymentsForm(initial=paypal_dict)
	 	return render(request, 'map/process_payment.html', {'order': car, 'form': form})

	#TODO: SET CORRECT URLS
	@csrf_exempt
	def payment_done(request):
	    return render(request, '')
	 
	#TODO: SET CORRECT URLS
	@csrf_exempt
	def payment_canceled(request):
	    return render(request, '')
	    return render(request, '')

class ConfirmationPage(TemplateView):
	template_name = 'confirmation/confirmation.html'

	def get(self, request, number_plate):
		print("GET METHOD")
		set_car = Car.objects.get(number_plate=number_plate)
		args = {
        	"car": set_car
    	}
		return render(request, self.template_name, args)
