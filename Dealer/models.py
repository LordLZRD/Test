from django.db import models
from django_countries.fields import CountryField


class Dealer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    year_of_foundation = models.IntegerField()
    amount_of_consumers = models.IntegerField()

    is_active = models.BooleanField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    def __str__(self):
        return self.name