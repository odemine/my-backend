from django.db import models

class Booking(models.Model):
    STATUS_CHOICES = [
        ('booking', 'Booking'),
        ('renting', 'Renting'),
        ('rented', 'Rented'),
    ]

    email = models.EmailField(max_length=254)
    vehicle = models.CharField(max_length=255)
    pickup_date = models.CharField(max_length=100)
    dropoff_date = models.CharField(max_length=100)
    
    # --- ADDED NEW DATABASE FIELDS FOR DASHBOARD SYNC ---
    unit_price = models.IntegerField(default=0)
    promo_code = models.CharField(max_length=50, blank=True, null=True, default="None")
    payment_method = models.CharField(max_length=50, default="cash")
    # ----------------------------------------------------

    total_cost = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.vehicle} ({self.status})"

