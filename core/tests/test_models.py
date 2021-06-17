from unittest.mock import patch

from django.test import TestCase

from core import models


class ModelTest(TestCase):

    def test_Client_str(self):
        """Test the Client string representation"""
        client = models.Client.objects.create(
            payer='test',
            points=500
        )

        self.assertEqual(str(client), client.payer)

    def test_PointBalance_str(self):
        """Test the PointBalance string representation"""
        pointBalance = models.PointBalance.objects.create(
            payer='test',
            points=500
        )

        self.assertEqual(str(pointBalance), pointBalance.payer)

    def test_SpendFinal_str(self):
        """Test the SpendFinal string representation"""
        spendFinal = models.SpendFinal.objects.create(
            payer='test',
            points=500
        )

        self.assertEqual(str(spendFinal), spendFinal.payer)