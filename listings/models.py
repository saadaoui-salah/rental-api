from django.db import models
from django.contrib.auth import get_user_model
from users.models import CustomUser
User = get_user_model()



# Create your models here.
class Listing(models.Model):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    RENT = "RENT"

    status_choices = [
        (PENDING, "Pending"),
        (ACTIVE, "Active"),
        (RENT, "Rent"),
        ]

    user = models.ForeignKey(User,limit_choices_to={'user_type':CustomUser.SELLER}, on_delete=models.CASCADE)
    price = models.FloatField(max_length=100)
    status = models.CharField(max_length=100, choices=status_choices)
    address = models.CharField(max_length=200)
    unit_number = models.CharField(max_length=200)


class DetailsSection(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)