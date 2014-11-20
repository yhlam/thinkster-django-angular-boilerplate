from django.contrib.auth import authenticate, get_user_model
from django.test import TestCase

from model_mommy import mommy

from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer


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


class UserSerializerTest(TestCase):
    def test_serialize_user(self):
        user = mommy.make(User)
        serializer = UserSerializer(user)
        self.assertEqual(user.id, serializer.data['id'])
        self.assertEqual(user.username, serializer.data['username'])
        self.assertEqual(user.email, serializer.data['email'])
        self.assertEqual(user.first_name, serializer.data['first_name'])
        self.assertEqual(user.last_name, serializer.data['last_name'])
        self.assertNotIn('password', serializer.data)

    def test_deserialize_user(self):
        user = mommy.prepare(User)
        serializer = UserSerializer(data={
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'password': user.password,
        })

        self.assertTrue(serializer.is_valid())
        self.assertEqual(user.username, serializer.object.username)
        self.assertEqual(user.email, serializer.object.email)
        self.assertEqual(user.first_name, serializer.object.first_name)
        self.assertEqual(user.last_name, serializer.object.last_name)

        serializer.save()
        user = authenticate(username=user.username, password=user.password)
        self.assertIsNotNone(user)
        self.assertTrue(user.is_active)


class UserProfileSerializerTest(TestCase):
    def test_serialize_user_profile(self):
        user = mommy.make(User)
        profile = user.profile
        serializer = UserProfileSerializer(profile)
        self.assertEqual(user.id, serializer.data['id'])
        self.assertEqual(user.username, serializer.data['username'])
        self.assertEqual(user.email, serializer.data['email'])
        self.assertEqual(user.first_name, serializer.data['first_name'])
        self.assertEqual(user.last_name, serializer.data['last_name'])
        self.assertEqual(profile.tagline, serializer.data['tagline'])
        self.assertEqual(profile.created_at, serializer.data['created_at'])
        self.assertEqual(profile.updated_at, serializer.data['updated_at'])
