from django.db import models

class Customer(models.Model):
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
    is_suspended = models.BooleanField(default=False)

    def __str__(self):
        return self.email