from django.forms import ModelForm
from .models import Item
from restaurant.models import RestaurantLocation

class ItemForm(ModelForm):
	class Meta:
		model = Item

		fields = [
			'name',
			'restaurant',
			'contents',
			'excludes',
			'public'
		]


	def __init__(self, user = None, **kwargs):
		print(user)
		super(ItemForm, self).__init__(**kwargs)
		self.fields['restaurant'].queryset = RestaurantLocation.objects.filter(owner = user)