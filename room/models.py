from django.db import models
from users.models import User

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=30, blank=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    room_image = models.ImageField(upload_to='room_image/%Y/%m/%d/', blank=True)
    max_guest = models.PositiveSmallIntegerField(default=1)
    memo = models.TextField(blank=True)

    def __str__(self):
        return self.name