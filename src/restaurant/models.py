from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from restaurant.utils import unique_slug_generator
from .validators import validate_location, validate_dish_name, validate_rl_name

User = settings.AUTH_USER_MODEL

# Create your models here.

class RestaurantLocation(models.Model):
	owner			= models.ForeignKey(User)
	name 			= models.CharField(max_length = 120, validators = [validate_rl_name])
	location 		= models.CharField(max_length = 120, null = True, blank = True, validators = [validate_location])
	
	CHOICES = (('Veg', 'Veg'), ('Non-veg', 'Non-veg'))
	category = models.CharField(max_length = 7,choices = CHOICES)

	timestamp		= models.DateTimeField(auto_now_add = True)
	updated			= models.DateTimeField(auto_now = True)
	slug 			= models.SlugField(null = True, blank = True)

	def __str__(self):
		return self.name


	@property
	def title(self):
		return self.name	


def  rl_pre_save_receiver(sender, instance, **kwargs):
 	instance.name = instance.name.capitalize()
 	instance.location = instance.location.capitalize()

 	if not instance.slug:
 		instance.slug = unique_slug_generator(instance)


pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)


class Dish(models.Model):
	name 		= models.CharField(max_length = 120, validators = [validate_dish_name])
	timestamp 	= models.DateTimeField(auto_now_add = True)
	updated 	= models.DateTimeField(auto_now = True)

	CHOICES = (
		('Veg', 'Veg'), 
		('Non-veg', 'Non-veg'),
	)
	category 	= models.CharField(max_length = 7, choices = CHOICES)
	slug		= models.SlugField(null = True, blank = True)

	def __str__(self):
		return self.name


	@property
	def title(self):
		return self.name


def dish_pre_save_receiver(sender, instance, **kwargs):
	instance.name = instance.name.capitalize()

	if not instance.slug:
		instance.slug = unique_slug_generator(instance)


pre_save.connect(dish_pre_save_receiver, sender = Dish)