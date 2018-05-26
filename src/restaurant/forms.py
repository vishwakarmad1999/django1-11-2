from django import forms
from .models import RestaurantLocation


class RestaurantCreateForm(forms.Form):
	name 			= forms.CharField()
	location 		= forms.CharField(required = False)
	
	CHOICES = (('Veg', 'Veg'), ('Non-veg', 'Non-veg'),)

	category = forms.ChoiceField(choices = CHOICES)


class RestaurantLocationCreateForm(forms.ModelForm):

	class Meta:
		model = RestaurantLocation

		fields = [
			'name',
			'location',
			'category',
			'slug'
		]

	def clean_slug(self):
		slug = self.cleaned_data.get('slug')

		qs = RestaurantLocation.objects.all()

		for obj in qs:
			if slug == obj.slug:
				forms.ValidationError('Please enter a unique slug')