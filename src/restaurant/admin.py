from django.contrib import admin

# Register your models here.
from .models import RestaurantLocation, Dish

admin.site.register(RestaurantLocation)
admin.site.register(Dish)	