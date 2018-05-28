from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.http import Http404
from restaurant.models import RestaurantLocation
from menu.models import Item

User = get_user_model()

# Create your views here.

class ProfileDetailView(DetailView):
	template_name = 'profile/user.html'

	def get_object(self):
		username = self.kwargs.get("username")

		if username is None:
			raise Http404
		return get_object_or_404(User, username__iexact = username, is_active = True)


	def get_context_data(self, **kwargs):
		context = super(ProfileDetailView, self).get_context_data(**kwargs)

		user = context['user']
		item_exists = Item.objects.filter(user = user).exists()
		qs = RestaurantLocation.objects.filter(owner = user)

		query = self.request.GET.get('q')

		if query:
			query = query.strip()
			qs = qs.search(query)

		if qs.exists() and item_exists:
			context['locations'] = qs

		return context
