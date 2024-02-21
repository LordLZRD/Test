from django.db import models
from django_countries.fields import CountryField


class Auto(models.Model):
    id = models.BigAutoField(primary_key=True)
    make = models.CharField(max_length=25)
    class_of_auto = models.CharField(max_length=1)  # BAR
    model = models.CharField(max_length=25)
    year = models.IntegerField()
    motor = models.CharField(max_length=10)  # BAR

    is_active = models.BooleanField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    def __str__(self):
        return f"{self.make} - {self.class_of_auto} - {self.year}"
