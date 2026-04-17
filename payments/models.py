from django.db import models
from guests.models import Guest
from rooms.models import Room

# Create your models here.

class Payment(models.Model):
    PAYMENT_TYPES = [
        ('Mobile', 'Mobile Money'),
        ('Card','card'),
        ('Cash', 'cash'),
    ]

    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=10, choices=PAYMENT_TYPES)
    payment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.guest} - {self.amount}"