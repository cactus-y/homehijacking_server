from django.db import models
from users.models import User

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=30, blank=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='host')
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name='guest')
    rsv_date = models.CharField(max_length=17)

    def __str__(self):
        return self.name