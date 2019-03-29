from django.db import models

# Create your models here.
class Car(models.Model):
	brand = models.CharField(max_length=20)
	transmission = models.CharField(max_length=20)
	numberplate = models.CharField(max_length=7)
	price = models.IntegerField()
	longitude = models.FloatField()
	latitude = models.FloatField()
	availble = models.BooleanField(default=True)

	def __init__