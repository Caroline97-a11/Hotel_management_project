from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Staff(AbstractUser):
    ROLES = [('MANAGER', 'manager'),('ATTENDANT', 'attendant')]
    roles = models.CharField(max_length=15, choices= ROLES)
    def __str__(self):
        return self.username

# class Usar(models.Model):
#     user_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     password = models.CharField()



