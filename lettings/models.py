from django.db import models
from oc_lettings_site.models import Address


class Letting(models.Model):
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "oc_lettings_site_letting"
