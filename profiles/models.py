from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model.
    Create a new profile with a User django and a favorite_city.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Set up a str username when called.
        :return: str username of the user.
        """
        return self.user.username

    class Meta:
        """
        DB saved at oc_lettings_cite_profile.
        """

        db_table = "oc_lettings_site_profile"
