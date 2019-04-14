from django.db import models
from django.contrib.auth.models import User

# Our Account Model
class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	book_status = models.BooleanField(default=False)