from .forms import ItemForm
from .models import Item
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

class HomeView(View):
	def get(self, request, **kwargs):
		if not request.user.is_authenticated():
			return render(request, "home.html", {})

		user = request.user

		is_following_user_ids = [x.user.id for x in user.is_following.all()]
		qs = Item.objects.filter(user__id__in = is_following_user_ids, public = True).order_by("user")

		user_ = False
		
		if self.request.GET.get("u"):
			searched_ = self.request.GET.get("u")
		
			user_ = User.objects.filter(username__icontains = searched_)

		context = {"object_list" : qs, "user_" : user_}

		return render(request, "menu/home-feed.html", context)

class ItemListView(LoginRequiredMixin, ListView):

	def get_queryset(self):
		print(self.request.user)
		return Item.objects.filter(user = self.request.user)

class ItemDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self):
		return Item.objects.filter(user = self.request.user)


class ItemCreateView(LoginRequiredMixin, CreateView):
	form_class = ItemForm
	template_name = 'form.html'

	def form_valid(self, form):
		instance = form.save(commit = False)
		instance.user = self.request.user
		return super(ItemCreateView, self).form_valid(form)


	def get_queryset(self):
		return Item.objects.filter(user = self.request.user)


	def get_form_kwargs(self):
		kwargs = super(ItemCreateView, self).get_form_kwargs()
		# kwargs['instance'] = Item.objects.filter(user = self.request.user).first()
		kwargs['user'] = self.request.user
		return kwargs


	def get_context_data(self, **kwargs):
		context = super(ItemCreateView, self).get_context_data(**kwargs)
		context['title'] = 'Add Item'
		return context


class ItemUpdateView(LoginRequiredMixin, UpdateView):
	form_class = ItemForm
	template_name = 'menu/update-detail.html'

	def get_queryset(self):
		return Item.objects.filter(user = self.request.user)


	def get_context_data(self, **kwargs):
		context = super(ItemUpdateView, self).get_context_data(**kwargs)
		context['title'] = 'Update Item'
		return context


	def get_form_kwargs(self):
		kwargs = super(ItemUpdateView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs