from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Room(models.Model):
    user_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_1")
    user_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_2")


class Message(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="from_user")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reciever")
    recieved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)