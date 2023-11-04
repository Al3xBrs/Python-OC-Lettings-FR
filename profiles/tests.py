from django.test import TestCase
from profiles.models import Profile
from django.contrib.auth.models import User
from django.urls import reverse


class CreateTestCase(TestCase):
    """
    Test create profile
    """

    def setUp(self):
        """
        Set up a Profile TEST
        """
        self.user = User.objects.create_user(username="TEST", password="TEST")
        self.profile_test = Profile.objects.create(user=self.user, favorite_city="TEST")

    def test_create_profile(self):
        """
        Assert equal profile is correctly displayed.
        """
        self.assertEqual(self.profile_test.user, self.user)
        self.assertEqual(self.profile_test.favorite_city, "TEST")

    def test_return_str(self):
        """
        Assert equal profile call is its username str.
        """
        self.assertEqual(str(self.profile_test), self.user.username)


class ViewsTestCase(TestCase):
    """
    Test urls for profiles.
    """

    def setUp(self):
        """
        Set up a profile.
        """
        self.user = User.objects.create_user(username="TEST", password="TEST")

    def test_profiles_index_response(self):
        """
        Test profiles index url. Should return status code 200.
        """
        url = reverse("profiles_index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_profile_response(self):
        """
        Test profile page url. Should return status code 200 with correct information.
        """
        profile_test = Profile.objects.create(user=self.user, favorite_city="TEST")
        username_profile = str(profile_test)
        url = reverse("profile", args=[username_profile])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
