from django.contrib.auth.hashers import make_password
from django.urls import reverse
from rest_framework.test import APITestCase

from main.apps.profiles.factories import ProfileFactory


class AuthenticationTest(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('backend:token-auth')

        self.profile = ProfileFactory(
            user__username='test',
            user__password=make_password('12345')
        )
        self.client.force_login(self.profile.user)

    def test_token_auth(self):
        data = {
            'username': 'test',
            'password': '12345'  # NOSONAR
        }
        response = self.client.post(
            path=self.url,
            data=data,
            format='json',
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue('refresh' in response_json)
        self.assertTrue('access' in response_json)
