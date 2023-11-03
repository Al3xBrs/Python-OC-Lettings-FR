from django.test import TestCase
from profiles.models import Profile
from django.contrib.auth.models import User


class CreateTestCase(TestCase):
    def test_create_profile(self):
        profile_test = Profile.objects.get(favorite_city="TEST")
        self.assertEqual(profile_test.favorite_city, "TEST")
