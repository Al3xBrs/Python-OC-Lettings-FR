from django.test import TestCase
from django.urls import reverse
from lettings.models import Letting, Address
from profiles.models import Profile
from django.contrib.auth.models import User


def test_dummy():
    assert 1


class UrlTestCase(TestCase):
    def setUp(self):
        self.address_test = Address.objects.create(
            number=999,
            street="Rue Du Python",
            city="Saint Python lès Dax",
            state="NA",
            zip_code=40999,
            country_iso_code="FRA",
        )
        self.letting_test = Letting.objects.create(
            title="Python HOUSE",
            address=self.address_test,
        )

        self.user = User.objects.create_user(username="TEST", password="TEST")
        self.profile_test = Profile.objects.create(user=self.user, favorite_city="TEST")

    def test_index(self):
        urls = [
            reverse("index"),
            reverse("lettings_index"),
            reverse("letting", args=[self.letting_test.id]),
            reverse("profiles_index"),
            reverse("profile", args=[str(self.profile_test)]),
        ]
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
