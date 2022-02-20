# Create your models here.

from django.db import models


class Destination(models.Model):
    """
    Model trip
    """
    id_destination = models.BigAutoField(primary_key=True)

    city_name = models.CharField(max_length=50, db_column='city')
    state = models.CharField(max_length=50, blank=True, null=True)
    switch = models.SmallIntegerField(null=True, blank=True, default='1')
    hotel = models.CharField(max_length=50, unique=True)
    hotel_address = models.CharField(max_length=50, unique=True)

    constraints = [
        models.UniqueConstraint(fields=['hotel', 'city_name'], name='unique city')
    ]

    def __str__(self):
        return f"{self.id_destination}, {self.city_name}, {self.hotel}" or f"{self.id_destination}, {self.city_name}"
