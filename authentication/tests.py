from django.contrib.auth import authenticate
from django.test import TestCase

from model_mommy import mommy
from model_mommy import generators

from .models import Account
from .serializers import AccountSerializer


class AccountSerializerTest(TestCase):
    def test_create_account(self):
        account = mommy.prepare(Account)

        serializer = AccountSerializer(data={
            'username': account.username,
            'email': account.email,
            'first_name': account.first_name,
            'last_name': account.last_name,
            'tagline': account.tagline,
            'password': account.password,
            'confirm_password': account.password,
        })

        self.assertTrue(serializer.is_valid(), str(serializer.errors))

        new_account = serializer.save()
        self.assertEqual(new_account.username, account.username)
        self.assertEqual(new_account.email, account.email)
        self.assertEqual(new_account.first_name, account.first_name)
        self.assertEqual(new_account.last_name, account.last_name)
        self.assertEqual(new_account.tagline, account.tagline)

        user = authenticate(email=account.email, password=account.password)
        self.assertIsNotNone(user)

    def test_update_tagline(self):
        account = mommy.make(Account)
        tagline = generators.gen_string(
            Account._meta.get_field('tagline').max_length
        )

        serializer = AccountSerializer(
            account,
            data={'tagline': tagline},
            partial=True,
        )

        self.assertTrue(serializer.is_valid(), str(serializer.errors))

        serializer.save()
        updated_account = Account.objects.get(pk=account.pk)
        self.assertEqual(updated_account.tagline, tagline)

    def test_cannot_update_email(self):
        account = mommy.make(Account)
        email = generators.gen_email()
        self.assertNotEqual(email, account.email)

        serializer = AccountSerializer(
            account,
            data={'email': email},
            partial=True,
        )

        self.assertTrue(serializer.is_valid(), str(serializer.errors))

        serializer.save()
        updated_account = Account.objects.get(pk=account.pk)
        self.assertEqual(updated_account.email, account.email)

    def test_cannot_update_username(self):
        account = mommy.make(Account)
        username = generators.gen_string(
            Account._meta.get_field('username').max_length
        )
        self.assertNotEqual(username, account.username)

        serializer = AccountSerializer(
            account,
            data={'username': username},
            partial=True,
        )

        self.assertTrue(serializer.is_valid(), str(serializer.errors))

        serializer.save()
        updated_account = Account.objects.get(pk=account.pk)
        self.assertEqual(updated_account.username, account.username)

    def test_update_password(self):
        old_password = generators.gen_string(8)
        new_password = generators.gen_string(8)
        self.assertNotEqual(old_password, new_password)

        account = mommy.make(Account)
        account.set_password(old_password)
        account.save()

        serializer = AccountSerializer(
            account,
            data={'password': new_password, 'confirm_password': new_password},
            partial=True,
        )

        self.assertTrue(serializer.is_valid(), str(serializer.errors))

        serializer.save()

        user = authenticate(email=account.email, password=new_password)
        self.assertIsNotNone(user)

    def test_password_mismatch(self):
        password = generators.gen_string(8)
        confirm_password = generators.gen_string(8)
        self.assertNotEqual(password, confirm_password)

        account = mommy.make(Account)
        serializer = AccountSerializer(
            account,
            data={'password': password, 'confirm_password': confirm_password},
            partial=True,
        )

        self.assertFalse(serializer.is_valid())
