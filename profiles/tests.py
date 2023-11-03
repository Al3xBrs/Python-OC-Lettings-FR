from django.test import TestCase
from profiles.models import Profile
from django.contrib.auth.models import User
from django.urls import reverse


class CreateTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="TEST", password="TEST")
        self.profile_test = Profile.objects.create(user=self.user, favorite_city="TEST")

    def test_create_profile(self):
        self.assertEqual(self.profile_test.user, self.user)
        self.assertEqual(self.profile_test.favorite_city, "TEST")

    def test_return_str(self):
        self.assertEqual(str(self.profile_test), self.user.username)


class ViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="TEST", password="TEST")

    def test_profiles_index_response(self):
        url = reverse("profiles_index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_profile_response(self):
        profile_test = Profile.objects.create(user=self.user, favorite_city="TEST")
        username_profile = str(profile_test)
        url = reverse("profile", args=[username_profile])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
