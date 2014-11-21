from django.contrib.auth import authenticate, get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase

from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase

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


class UserCreateViewTest(APITestCase):
    def test_create_user(self):
        user = mommy.prepare(User)
        response = self.client.post(
            reverse('user-create'),
            {
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'password': user.password,
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(user.username, response.data['username'])
        self.assertEqual(user.email, response.data['email'])
        self.assertEqual(user.first_name, response.data['first_name'])
        self.assertEqual(user.last_name, response.data['last_name'])

        try:
            db_user = User.objects.get(id=response.data['id'])
        except User.DoesNotExist:
            self.fail('User is not created')

        self.assertEqual(db_user.id, response.data['id'])
        self.assertEqual(db_user.username, response.data['username'])
        self.assertEqual(db_user.email, response.data['email'])
        self.assertEqual(db_user.first_name, response.data['first_name'])
        self.assertEqual(db_user.last_name, response.data['last_name'])


class CurrentUserViewTest(APITestCase):
    def test_get_login_user(self):
        user = mommy.prepare(User)
        password = user.password
        user.set_password(password)
        user.save()

        self.client.login(username=user.username, password=password)

        response = self.client.get(reverse('user-me'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], user.username)
        self.assertEqual(response.data['email'], user.email)
        self.assertEqual(response.data['first_name'], user.first_name)
        self.assertEqual(response.data['last_name'], user.last_name)

    def test_fail_when_not_login(self):
        response = self.client.get(reverse('user-me'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

