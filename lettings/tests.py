from django.test import TestCase
from lettings.models import Letting, Address
from django.urls import reverse


class CreateTestCase(TestCase):
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

    def test_create_address(self):
        self.assertEqual(self.address_test.number, 999)
        self.assertEqual(self.address_test.street, "Rue Du Python")
        self.assertEqual(self.address_test.city, "Saint Python lès Dax")
        self.assertEqual(self.address_test.state, "NA")
        self.assertEqual(self.address_test.zip_code, 40999)
        self.assertEqual(self.address_test.country_iso_code, "FRA")

    def test_return_address_str(self):
        self.assertEqual(str(self.address_test), "999 Rue Du Python")

    def test_create_letting(self):
        self.assertEqual(self.letting_test.title, "Python HOUSE")
        self.assertEqual(self.letting_test.address, self.address_test)

    def test_return_letting_str(self):
        self.assertEqual(str(self.letting_test), "Python HOUSE")


class ViewsTestCase(TestCase):
    def setUp(self):
        address_test = Address.objects.create(
            number=999,
            street="Rue Du Python",
            city="Saint Python lès Dax",
            state="NA",
            zip_code=40999,
            country_iso_code="FRA",
        )
        Letting.objects.create(
            title="Python HOUSE",
            address=address_test,
        )

    def test_lettings_index_response(self):
        url = reverse("lettings_index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_letting_response(self):
        letting_test = Letting.objects.get(title="Python HOUSE")
        id_test = letting_test.id
        url = reverse("letting", args=[id_test])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
