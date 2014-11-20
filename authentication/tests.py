from django.contrib.auth import get_user_model
from django.test import TestCase

from model_mommy import mommy

from .models import UserProfile


User = get_user_model()


class UserProfileSignalTest(TestCase):
    def test_auto_create_user_profile_after_create_user(self):
        user = mommy.prepare(User)

        with self.assertRaises(UserProfile.DoesNotExist):
            UserProfile.objects.get(user=user)

        user.save()

        try:
            UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            self.fail('UserProfile is not created automatically after '
                      'creating a User')

    def test_auto_delete_user_profile_after_before_user(self):
        user = mommy.make(User)

        try:
            UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            self.fail('UserProfile is not created')

        user.delete()

        with self.assertRaises(UserProfile.DoesNotExist):
            UserProfile.objects.get(user=user)
