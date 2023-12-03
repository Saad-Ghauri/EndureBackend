from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    vendor_number = models.CharField(max_length=50)
    price = models.CharField(max_length=255)
    additional_terms = models.TextField()
    representatives = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    def __str__(self):
        return self.name