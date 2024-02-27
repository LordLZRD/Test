from django.db import models
from django_countries.fields import CountryField


class SaloonHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    auto_list_id = models.ForeignKey('AutoList.AutoList', on_delete=models.PROTECT, null=True)
    consumer_id = models.ForeignKey('Consumer.Consumer', on_delete=models.PROTECT, null=True)
    saloon_id = models.ForeignKey('Saloon.Saloon', on_delete=models.PROTECT, null=True)

    is_active = models.BooleanField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    def __str__(self):
        return f"{self.date} - {self.auto_list_id} - {self.consumer_id} - {self.saloon_id}"