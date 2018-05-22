from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import RestaurantLocation, Dish
from .forms import RestaurantLocationCreateForm, DishModelCreateForm

# Create your views here.

class RestaurantLocationCreateView(LoginRequiredMixin, CreateView):
	form_class = RestaurantLocationCreateForm
	template_name = 'restaurant/form.html'
	# success_url = '/restaurant'
	# login_url = '/login'

	def form_valid(self, form):
		instance = form.save(commit = False)

		instance.owner = self.request.user

		return super(RestaurantLocationCreateView, self).form_valid(form)


class SearchRestaurantListView(ListView):
	def get_queryset(self):
		slug = self.kwargs.get("slug")

		if slug:
			queryset = RestaurantLocation.objects.filter(
				Q(category__iexact = slug)
				)
		else:
			queryset = RestaurantLocation.objects.all()

		return queryset


class SearchRestaurantDetailView(DetailView):
	queryset = RestaurantLocation.objects.all()


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


# Generic List View

#----------------Views for Dish-------------------------

class DishListView(ListView):
	template_name = 'dish/dish_list.html'

	queryset = Dish.objects.all()


class DishDetailView(DetailView):
	template_name = 'dish/dish_detail.html'

	queryset = Dish.objects.all()

	# def get_object(self, **kwargs):
	# 	obj = get_object_or_404(Dish, pk = self.kwargs.get("id"))
	# 	return obj

class DishCreateView(LoginRequiredMixin, CreateView):
	form_class = DishModelCreateForm
	template_name = 'dish/form.html'
	login_url = '/login'

	def form_valid(self, form):
		instance = form.save(commit = False)
		instance.owner = self.request.user

		return super(DishCreateView, self).form_valid(form)


# @login_required()
# def dish_createview(request):
# 	form = DishModelCreateForm(request.POST or None)
# 	errors = None

# 	if form.is_valid():
# 		if request.user.is_authenticated():
# 			instance = form.save(commit = False)
# 			instance.owner = request.user
# 			instance.save()

# 			return HttpResponseRedirect('/dish')
# 	else:
# 		errors = form.errors

# 	context = {
# 		"form" : form,
# 		"errors" : errors,
# 	}	

# 	template_name = 'dish/form.html'

# 	return render(request, template_name, context)