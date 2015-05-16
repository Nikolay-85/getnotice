from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class AccountTests(APITestCase):
    def test_create_message(self):
        """
        Ensure we can create a new message object.
        """
        url = reverse('messages_api')
        data = {
            'text': 'He there',
            'level': 'silent'
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)

    def test_create_invalid_message(self):
        """
        Ensure we can create a new message object with a huge text.
        """
        url = reverse('messages_api')
        data = {
            'text': 'H'*10000,
            'level': 'silent'
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEquals(response.data, data)