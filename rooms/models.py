from django.db import models

# Create your models here.
class RoomType(models.Model):
    name = models.CharField(max_length=20, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    room_category = models.ForeignKey(
        RoomType,
        on_delete=models.CASCADE
    )
    room_status = models.CharField(max_length=20, default='available')