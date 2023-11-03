from django.test import TestCase
from profiles.models import Profile


class CreateTestCase(TestCase):
    def test_create_profile(self):
        profile_test = Profile.objects.get(user_id=5)
        self.assertEqual(profile_test.user_id, 5)
