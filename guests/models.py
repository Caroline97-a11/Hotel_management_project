from django.db import models

# Create your models here.
class Guest(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(max_length=15, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    date_registered = models.DateField(blank=False, null=False)
    guest_status=models.CharField(max_length=20, blank=False, default='checked in')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"