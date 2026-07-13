from django.db import models

class PromoCode(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=100, default="Promo Deal") # <-- Added field
    codename = models.CharField(max_length=50, unique=True)
    discount_percentage = models.PositiveIntegerField()
    condition = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.codename}) - {self.discount_percentage}%"