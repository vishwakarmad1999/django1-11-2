from .forms import ItemForm
from .models import Item
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

# Create your views here.

class ItemListView(LoginRequiredMixin, ListView):

	def get_queryset(self):
		print(self.request.user)
		return Item.objects.filter(user = self.request.user)

class ItemDetailView(DetailView):
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
	template_name = 'form.html'

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