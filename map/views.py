from django.shortcuts import render
from django.http import HttpResponse
from map.models import Car
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView

class HomePageView(TemplateView):
	template_name = 'map/homepage.html'

	def get_context_data(self, *args, **kwargs):
		context = super(HomePageView, self).get_context_data(*args, **kwargs)
		context['cars'] = Car.objects.filter(available=True)
		return context
