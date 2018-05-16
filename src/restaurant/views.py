import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

# Create your views here.

# Class based view (Base -> View)
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


class HomeView(TemplateView):
	template_name = "home.html"

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)	

		num = random.randint(0, 1000)

		context = {"lang" : "Python, yes...", 
					"num" : num, 
					"bool_item" : True,
					"list" : list(range(num))}

		return context


class Creator_2_View(TemplateView):
	template_name = 'creator2.html'

	def get_context_data(self, **vargs):
		context = super(Creator_2_View, self).get_context_data(**vargs)

		context = {
			"lang" : "Python"
		}

		return context