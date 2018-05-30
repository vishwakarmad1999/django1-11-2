from django.db import models
from django.db.models.signals import post_save
from django.conf import settings


User = settings.AUTH_USER_MODEL

# Create your models here.

class ProfileManager(models.Manager):
	def toggle_follow(self, request_user, username_to_toggle):
		profile_ = Profile.objects.get(user__username__iexact = username_to_toggle)
		user = request_user

		is_following = False

		if user in profile_.followers.all():
			profile_.followers.remove(user)
		else:
			profile_.followers.add(user)
			is_following = True

		return profile_, is_following

class Profile(models.Model):
	# Relation keys
	user		= models.OneToOneField(User)
	followers	= models.ManyToManyField(User, related_name = 'is_following', blank = True)
	# following 	= models.ManyToManyField(User, related_name = 'following', blank = True)

	# Actual keys
	timestamp	= models.DateTimeField(auto_now_add = True)
	updated		= models.DateTimeField(auto_now = True)
	activated	= models.BooleanField(default = False)

	objects = ProfileManager()

	def __str__(self):
		return self.user.username


def post_save_user_receiver(sender, instance, created, **kwargs):
	if created:
		profile, is_created = Profile.objects.get_or_create(user = instance)

	default_user_profile = Profile.objects.first()
	default_user_profile.followers.add(instance) # This will add newly created user to the followers list of user with id = 1
	profile.followers.add(default_user_profile.user)
post_save.connect(post_save_user_receiver, sender = User)