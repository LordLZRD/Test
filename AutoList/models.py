from django.db import models
from django_countries.fields import CountryField


class AutoList(models.Model):
    id = models.BigAutoField(primary_key=True)
    serial_number = models.CharField(max_length=40)
    auto_id = models.ForeignKey('Auto', on_delete=models.PROTECT, null=True)

    is_active = models.BooleanField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    def __str__(self):
        return f"{self.serial_number} - {self.auto_id}"