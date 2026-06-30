from django.db import models

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=20)  # ev, fuel, bike
    image = models.CharField(max_length=255)
    price = models.IntegerField()
    badge_icon = models.CharField(max_length=50)
    badge_label = models.CharField(max_length=50)

    # 🚀 ADD THIS META BLOCK BELOW:
    class Meta:
        app_label = 'BACKEND'

    def __str__(self):
        return self.name