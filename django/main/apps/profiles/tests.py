from django.urls import reverse
from rest_framework.test import APITestCase

from main.apps.authentication.factories import UserFactory
from main.apps.profiles.choices import Role
from main.apps.profiles.factories import ProfileFactory


class ProfileTest(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.client.force_login(self.user)
        self.url = reverse('backend:profile-list')

    def test_create_profile(self):
        data = {
            'user': {
                'first_name': 'first_name',
                'last_name': 'last_name',
                'username': 'test',
                'password': '12345',  # NOSONAR
                'email': 'test@example.com',
            },
            'role': Role.GENERAL,
        }
        response = self.client.post(
            path=self.url,
            data=data,
            format='json',
        )

        self.assertEqual(response.status_code, 201)  # can create profile and user

    def test_update_profile(self):
        profile = ProfileFactory()

        data = {
            'role': Role.ACCOUNTING
        }

        response = self.client.patch(
            path=self.url + f'{profile.id}/',
            data=data,
            format='json',
        )

        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertEqual(
            response_json['role'],
            3
        )

    def test_delete_profile(self):
        profile = ProfileFactory()
        response = self.client.delete(
            path=self.url + f'{profile.id}/',
        )
        self.assertEqual(response.status_code, 204)  # can delete profile

    def test_list_profile(self):

        # create multiple profiles
        ProfileFactory.create_batch(10)

        # normal list
        response = self.client.get(
            path=self.url,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['results']), 10)
