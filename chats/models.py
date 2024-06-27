from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Room(models.Model):
    user_1 = models.ForeignKey(User, on_delete=models.CASCADE)
    user_2 = models.ForeignKey(User, on_delete=models.CASCADE)


class Message(mdoels.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE)
    recieved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)