from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Offer(models.Model):
    CASH = "CASH"
    FINANCING = "FINANCING"

    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    
    offer_type_choices = [
        (CASH,"CASH"),
        (FINANCING,"FINANCING"),
    ]

    reply_choices = [
        (ACCEPTED,"ACCEPTED"),
        (REJECTED,"REJECTED"),
    ]

    listing = models.ForeignKey("listings.Property", on_delete=models.CASCADE, related_name="listing")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer')
    client_price = models.IntegerField()
    closing_date = models.DateField()
    canceled_at = models.DateField()
    offer_type = models.CharField(max_length=200, choices=offer_type_choices)
    reply_type = models.CharField(max_length=200, choices=reply_choices)
    replied_at = models.DateField()