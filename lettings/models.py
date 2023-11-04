from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Address model.
    Create an address.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self) -> str:
        """
        :return: str number and street.
        """
        return f"{self.number} {self.street}"

    class Meta:
        """
        DB saved on oc_lettings_site_address table.
        Plural name Addresses in admin site.
        """

        db_table = "oc_lettings_site_address"
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Letting model.
    Create a letting with an address previously created.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        :return: str title of the letting.
        """
        return self.title

    class Meta:
        """
        DB saved in oc_lettings_site_letting table.
        """

        db_table = "oc_lettings_site_letting"
