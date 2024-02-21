from django.db import models

class Consumer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=4)
    number_of_purchases = models.IntegerField()

    is_active = models.BooleanField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    def __str__(self):
        return self.name
