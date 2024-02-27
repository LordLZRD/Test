from django.db import models
from django_countries.fields import CountryField


class Stock(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    begin = models.DateField()
    end = models.DateField()
    saloon_id = models.ForeignKey('Saloon.Saloon', on_delete=models.PROTECT, null=True)

    is_active = models.BooleanField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    def __str__(self):
        return self.name