from django.shortcuts import render, redirect
from django.http import HttpResponse
from map.models import Car
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView

from map.forms import CarForm

class HomePageView(TemplateView):
	template_name = 'map/homepage.html'

	def get_context_data(self, *args, **kwargs):
		context = super(HomePageView, self).get_context_data(*args, **kwargs)
		context['cars'] = Car.objects.filter(available=True)
		return context

	def car_post(self, request):
		if request.method == "POST":
			print("POST")

		return render(request, self.template_name, args)


	# def car_detail_view(request, id):
	# 	if request.method == "POST":
	# 		form = CarForm(request.POST)
	# 		if form.is_valid():
	# 			car_save = form.instance
	# 			get_car = Car.objects.get(number_plate=car_save.number_plate)
	# 			get_car.available = False
	# 			get_car.save()
	# 			return redirect('/')
	# 		else:
	# 			print(form.errors)
	# 	else:
	# 		car = Car.objects.get(id=id)
	# 		form = CarForm(initial={'brand':car.brand, 'number_plate':car.number_plate, 'price':car.price,
	# 							'available':car.available})
	# 		args = {
	# 			'car':car,
	# 			'form':form
	# 		}
		# return render(request, 'map/confirmation.html', args)
