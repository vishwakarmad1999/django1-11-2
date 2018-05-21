from django import forms
from .models import RestaurantLocation, Dish


class RestaurantCreateForm(forms.Form):
	name 			= forms.CharField()
	location 		= forms.CharField(required = False)
	
	CHOICES = (('Veg', 'Veg'), ('Non-veg', 'Non-veg'),)

	category = forms.ChoiceField(choices = CHOICES)


class DishCreateForm(forms.Form):
	name 		= forms.CharField()

	CHOICES = (
		('Veg', 'Veg'), 
		('Non-veg', 'Non-veg'),
	)

	category 	= forms.ChoiceField(choices = CHOICES)


class RestaurantLocationCreateForm(forms.ModelForm):

	class Meta:
		model = RestaurantLocation

		fields = [
			'name',
			'location',
			'category',
		]



class DishModelCreateForm(forms.ModelForm):

	class Meta:
		model = Dish

		fields = [
			'name',
			'category',
		]


	# def clean_name(self):
	# 	name = self.cleaned_data.get("name")

	# 	if name == "Beef":
	# 		raise forms.ValidationError('Bajrang dal')
	# 	return clean_name