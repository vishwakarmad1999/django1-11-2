from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from restaurant.utils import unique_slug_generator
from .validators import validate_location, validate_rl_name


User = settings.AUTH_USER_MODEL

# Create your models here.

class RestaurantLocationQuerySet(models.query.QuerySet):
	def search(self, query):
		return self.filter(
			Q(name__icontains = query) |
			Q(category__icontains = query) |
			Q(location__icontains = query) |
			Q(item__name__icontains = query) |
			Q(item__contents__icontains = query) 
			).distinct()


class RestauratLocationManager(models.Manager):
	def get_queryset(self):
		return RestaurantLocationQuerySet(self.model, using = self._db)


	def search(self, query):
		return self.get_queryset().search(query)


class RestaurantLocation(models.Model):
	owner			= models.ForeignKey(User)
	name 			= models.CharField(max_length = 120, validators = [validate_rl_name])
	location 		= models.CharField(max_length = 120, null = True, blank = True, validators = [validate_location])
	
	CHOICES = (('Veg', 'Veg'), ('Non-veg', 'Non-veg'))
	category = models.CharField(max_length = 7,choices = CHOICES)

	timestamp		= models.DateTimeField(auto_now_add = True)
	updated			= models.DateTimeField(auto_now = True)
	slug 			= models.SlugField(null = True, blank = True)

	objects = RestauratLocationManager()

	def __str__(self):
		return self.name


	@property
	def title(self):
		return self.name	


	def get_absolute_url(self):
		return reverse('restaurant:detail', kwargs={'slug' : self.slug})


	def get_absolute_update(self):
		return reverse('restaurant:update', kwargs={'slug' : self.slug})


def  rl_pre_save_receiver(sender, instance, **kwargs):
 	instance.name = instance.name.capitalize()
 	instance.location = instance.location.capitalize()

 	if not instance.slug:
 		instance.slug = unique_slug_generator(instance)


pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)