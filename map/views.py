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

# class HomePageView(ListView):
#     template_name = 'map/homepage.html'
#     queryset = Car.objects.filter(available=True)
#     context_object_name = 'cars'
#
#     def get_queryset(self):
#         return Car.objects.filter(available=True)

# class HomePageView(View):
#     template_name = 'map/homepage.html'
#
#     def get(self, request, *args, **kwargs):
#         # Get all car objects from db
#         cars = Car.objects.filter(available=True)
#
#         # Argument to contain list of our car model
#         context = {'cars': cars}
#         return render(request, self.template_name, context=context)

# def get_mylocation(request):
#     if request.GET.get('find-me'):
#         longitude = request.COOKIES.get('longitude', '')
#         latitude = request.COOKIES.get('latitude', '')
#     return render(request, 'map/homepage.html',
#                 {'longitude' :longitude,
#                  'latitude' :latitude})
