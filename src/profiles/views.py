from django.views.generic import CreateView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.http import Http404
from restaurant.models import RestaurantLocation
from menu.models import Item
from .models import Profile
from .forms import RegisterForm

User = get_user_model()

# Create your views here.

def activate_user_view(self, code = None, **kwargs):
	if code:
		qs = Profile.objects.filter(activation_key = code)

		if qs.exists() and qs.count() == 1:
			profile = qs.first()

			if not profile.activated:
				user_ = profile.user
				user_.is_active = True
				user_.save()

				profile.activated = True
				profile.activation_key = None
				profile.save()

				return HttpResponseRedirect("/login")

		return HttpResponseRedirect("/login")


class RegisterView(CreateView):
	form_class = RegisterForm
	template_name = "registration/register.html"
	success_url = "/login"

	def dispatch(self, *args,**kwargs):
		if self.request.user.is_authenticated():
			return HttpResponseRedirect("/")

		return super(RegisterView, self).dispatch(*args, **kwargs)


class ProfileFollowToggle(LoginRequiredMixin, View):
	def post(self, request, **kwargs):
		username_to_toggle = request.POST.get("username")
		profile_, is_following = Profile.objects.toggle_follow(request.user, username_to_toggle)
		return HttpResponseRedirect(f'/u/{profile_.user.username}')


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

		is_following = False

		if user.profile in self.request.user.is_following.all():
			is_following = True

		context['is_following'] = is_following

		if query:
			query = query.strip()
			qs = qs.search(query)

		if qs.exists() and item_exists:
			context['locations'] = qs

		return context
