from django.db import models

# Create your models here.

class RestaurantLocation(models.Model):
	name 			= models.CharField(max_length = 120)
	location 		= models.CharField(max_length = 120, null = True, blank = True)

	FRESHMAN = 'FR'
	SOPHOMORE = 'SO'
	JUNIOR = 'JR'
	SENIOR = 'SR'

	YEAR_IN_SCHOOL_CHOICES = (
		(FRESHMAN, 'Freshman'),
		(SOPHOMORE, 'Sophomore'),
		(JUNIOR, 'Junior'),
		(SENIOR, 'Senior'),
	)

	year_in_school = models.CharField(max_length = 2, choices = YEAR_IN_SCHOOL_CHOICES, default = FRESHMAN, )