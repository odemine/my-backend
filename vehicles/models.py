from django.db import models

class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, default="ev") # ev, fuel, bike
    price = models.IntegerField()
    image = models.CharField(max_length=500, blank=True, default="/image/xiaomi-su7.jpg")

    def __str__(self):
        return self.name