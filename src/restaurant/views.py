from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, UpdateView, ListView, DetailView, CreateView
from .models import RestaurantLocation
from .forms import RestaurantLocationCreateForm

# Create your views here.

class RestaurantLocationCreateView(LoginRequiredMixin, CreateView):
	form_class = RestaurantLocationCreateForm
	template_name = 'form.html'
	# success_url = '/restaurant'
	# login_url = '/login'

	def form_valid(self, form):
		instance = form.save(commit = False)

		instance.owner = self.request.user

		return super(RestaurantLocationCreateView, self).form_valid(form)


	def get_context_data(self, **kwargs):
		context = super(RestaurantLocationCreateView, self).get_context_data(**kwargs)
		context['title'] = 'Add Restaurant'
		return context


class SearchRestaurantListView(LoginRequiredMixin, ListView):
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner = self.request.user)


class SearchRestaurantDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner = self.request.user)


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
	form_class = RestaurantLocationCreateForm
	template_name = 'restaurant/update-detail.html'

	def get_context_data(self, **kwargs):
		context = super(RestaurantUpdateView, self).get_context_data(**kwargs)
		name = self.get_object().name
		context['title'] = f'Update : {name}'
		return context


	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner = self.request.user)

# Class based view (Base -> View)

class HomeView(View):
	def get(self, request, **vargs):
		return render(request, "home.html", {"lang" : "Python",})


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


