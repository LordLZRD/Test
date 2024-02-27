from django.db import models
from django_countries.fields import CountryField


class Offer(models.Model):
    id = models.BigAutoField(primary_key=True)
    auto_id = models.ForeignKey('Auto.Auto', on_delete=models.PROTECT)  # How to choose a car?
    max_money_offer = models.DecimalField(decimal_places=2, max_digits=20)
    consumer_id = models.ForeignKey('Consumer.Consumer', on_delete=models.PROTECT, null=True)

    is_active = models.BooleanField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    def __str__(self):
        return f"{self.auto_id} - {self.max_money_offer} - {self.consumer_id}"