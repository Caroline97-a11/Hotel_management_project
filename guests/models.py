from django.db import models
from rooms.models import Room

# Create your models here.
class Guest(models.Model):
        STATUS_CHOICES = [
        ('checked_in', 'Checked In'),
        ('checked_out', 'Checked Out'),
    ]
        first_name = models.CharField(max_length=100, blank=False, null=False)
        last_name = models.CharField(max_length=100, blank=False, null=False)
        phone_number = models.CharField(max_length=15, blank=False, null=False)
        email = models.EmailField(unique=True, blank=False, null=False)
        date_registered = models.DateField(blank=False, null=False)
        room_number = models.ForeignKey(Room, on_delete=models.SET_NULL,null=True, blank=True)
        guest_status=models.CharField(max_length=20, blank=False, choices=STATUS_CHOICES, default='checked_in')

        def __str__(self):
            return f"{self.first_name} {self.last_name}"