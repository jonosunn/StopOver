from django.contrib.auth.models import User
from user.models import Account
from django.db.models.signals import post_save
from django.dispatch import receiver

# Everytime a User is created, create an Account object for it
@receiver(post_save, sender=User)
def create_account(sender, instance, created, **kwargs):
    if created:
    	Account.objects.create(user=instance)

# Save the account object associated with the User
@receiver(post_save, sender=User)
def save_account(sender, instance, **kwargs):
        instance.account.save()