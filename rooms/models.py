from django.db import models

# Create your models here.
class RoomType(models.Model):
    category = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.category


class Room(models.Model):
    STATUS_CHOICES =[('Available','AVAILABLE'), ('Not_available', 'NOT_AVAILABLE')]

    room_number = models.CharField(max_length=10, unique=True)
    room_category = models.ForeignKey(
        RoomType,
        on_delete=models.CASCADE
    )
    room_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    def __str__(self):
        return self.room_number