from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_location(value):
	if value == 'Pakistan':
		raise ValidationError('We do not promote terrorism')

def validate_dish_name(value):
	value = value.capitalize()

	if value == 'Beef':
		raise ValidationError('Bajrang dal coming soon')

def validate_rl_name(value):
	value = value.capitalize()

	if value == "Hello":
		raise ValidationError("Ye kaisa name h?")

