from django.db import models
from django_countries.fields import CountryField


class Saloon(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    country = CountryField()
    balance = models.DecimalField(max_digits=10, decimal_places=4)
    characteristics = models.JSONField()

    is_active = models.BooleanField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    def __str__(self):
        return self.name

