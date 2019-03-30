from django.db import models

# Create your models here.
class Car(models.Model):
	brand = models.CharField(max_length=20)
	transmission = models.CharField(max_length=20)
	number_plate = models.CharField(max_length=7)
	price = models.IntegerField()
	longitude = models.FloatField()
	latitude = models.FloatField()
	available = models.BooleanField(default=True)

	def __str__(self):
		return self.number_plate