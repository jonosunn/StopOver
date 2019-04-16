from django.db import models
from django.urls import reverse

# Our Car Model
class Car(models.Model):
	brand = models.CharField(max_length=20)
	transmission = models.CharField(max_length=20)
	number_plate = models.CharField(max_length=7)
	price = models.IntegerField()
	longitude = models.FloatField()
	latitude = models.FloatField()
	available = models.BooleanField(default=True)

	def get_absolute_url(self):
		return reverse("confirmation", kwargs={"number_plate": self.number_plate})
		# f"/confirmation/{self.number_plate}"
