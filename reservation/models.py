from django.db import models
from users.models import User

# Create your models here.
class Reservation(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='host')
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name='guest')
    rsv_start_date = models.CharField(max_length=17)
    rsv_end_date = models.CharField(max_length=17)

    def __str__(self):
        return self.host.username + "'s reservation"
