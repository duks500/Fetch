from django.urls import reverse
from django.test import TestCase

from core.models import Client

from rest_framework import status
from rest_framework.test import APIClient


INGREDIENTS_URL = reverse('app:add-transaction')


class PublicAppApiTests(TestCase):
    """Test the publicly available API"""

    def setUp(self):
        self.client = APIClient()

    def test_create_Client_successful(self):
        """Test create a new Client"""
        payload = {
            'payer': 'Test',
            'points': 500,
        }
        self.client.post(INGREDIENTS_URL, payload)

        exists = Client.objects.filter(
            payer='Test',
            points=500
        ).exists()

        self.assertTrue(exists)