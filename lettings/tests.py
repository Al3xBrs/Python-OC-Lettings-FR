from django.test import TestCase
from lettings.models import Letting, Address
from django.urls import reverse


class CreateTestCase(TestCase):
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

    def test_create_address(self):
        address_test = Address.objects.get(street="Rue Du Python")
        self.assertEqual(address_test.number, 999)
        self.assertEqual(address_test.street, "Rue Du Python")
        self.assertEqual(address_test.city, "Saint Python lès Dax")
        self.assertEqual(address_test.state, "NA")
        self.assertEqual(address_test.zip_code, 40999)
        self.assertEqual(address_test.country_iso_code, "FRA")

    def test_create_letting(self):
        address_test = Address.objects.get(street="Rue Du Python")
        letting_test = Letting.objects.get(title="Python HOUSE")
        self.assertEqual(letting_test.title, "Python HOUSE")
        self.assertEqual(letting_test.address, address_test)


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

    def test_letting_index_response(self):
        lettings_list = Letting.objects.all()
        url = reverse("lettings_index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        self.assertQuerysetEqual(
            response.context["lettings_list"],
            lettings_list,
            transform=repr,
        )

    def test_index_response(self):
        letting_test = Letting.objects.get(title="Python HOUSE")
        id_test = letting_test.id
        # TODO:
        url = reverse("letting", args=[id_test])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
