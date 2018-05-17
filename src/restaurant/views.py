from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from .models import RestaurantLocation

# Create your views here.

# Function based view
'''	
def restaurant_listview(request):
	template_name = 'restaurants/restaurant_list.html'

	queryset = RestaurantLocation.objects.all()

	context = {
		"object_list" : queryset
	}

	return render(request, template_name, context)
'''


# Class based view (Base -> View)

class HomeView(View):
	def get(self, request, **vargs):
		return render(request, "home.html", {})


class ContactView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "contact.html", {})


# Class based view (Base -> TemplateView)

class AboutView(TemplateView):
	template_name = 'about.html'


class CreatorView(TemplateView):
	template_name = 'creator.html'

	def get_context_data(self, **kwargs): # This is method overriding 
		context = super(CreatorView, self).get_context_data(**kwargs)

		context = {"lang" : "Python"}

		return context


class Creator_2_View(TemplateView):
	template_name = 'creator2.html'

	def get_context_data(self, **vargs):
		context = super(Creator_2_View, self).get_context_data(**vargs)

		context = {
			"lang" : "Python"
		}

		return context


# Generic List View

class RestaurantListView(ListView):
	queryset = RestaurantLocation.objects.all()

	template_name = 'restaurants/restaurant_list.html'


class VegRestaurantListView(ListView):
	queryset = RestaurantLocation.objects.filter(category__iexact = 'veg only')

	template_name = 'restaurants/restaurant_list.html'


class NonVegRestaurantListView(ListView):
	queryset = RestaurantLocation.objects.filter(category__iexact = 'veg & non-veg')

	template_name = 'restaurants/restaurant_list.html'