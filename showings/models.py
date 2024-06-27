from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Offer(models.Model):
    IN_PERSON = "IN_PERSON"
    VIRTUAL = "VIRTUAL"

    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    
    meeting_type_choices = [
        (IN_PERSON,"IN_PERSON"),
        (VIRTUAL,"VIRTUAL"),
    ]

    reply_choices = [
        (ACCEPTED,"ACCEPTED"),
        (REJECTED,"REJECTED"),
    ]

    listing = models.ForeignKey("listings.Property", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client_price = models.IntegerField()
    meeting_date = models.DateTimeField()
    canceled_at = models.DateField()
    meeting_type = models.CharField(max_length=200, choices=meeting_type_choices)
    reply_type = models.CharField(max_length=200, choices=reply_choices)
    replied_at = models.DateField()