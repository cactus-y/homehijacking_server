from django.db import models
from users.models import User

# Create your models here.
class Reservation(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    rsv_date = models.CharField(max_length=12)