import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from tracker.models import Spending
from tracker.serializers import SpendingSerializer

client = Client()

class GetAllSpendingsTest(TestCase):
    def setUp(self):
        Spending.objects.create(
            amount=1000, currency="HUF", description="Food"
        )
        Spending.objects.create(
            amount=500, currency="USD", description="Rent"
        )
        Spending.objects.create(
            amount=15, currency="EUR", description="Bills"
        )

    def test_get_all_spendings(self):
        response = client.get(reverse('get-post-spending'))

        spendings = Spending.objects.all()
        serializer = SpendingSerializer(spendings, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetOneSpendingsTest(TestCase):
    def setUp(self):
        self.huf_spending = Spending.objects.create(
            amount=1000, currency="HUF", description="Food"
        )
        self.usd_spending = Spending.objects.create(
            amount=500, currency="USD", description="Rent"
        )
        self.eur_spending = Spending.objects.create(
            amount=15, currency="EUR", description="Bills"
        )

    def test_get_valid_spending(self):
        response = client.get(reverse('get-put-delete-spending', kwargs={'id': self.huf_spending.pk}))

        spending = Spending.objects.get(pk=self.huf_spending.pk)
        serializer = SpendingSerializer(spending)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_spending(self):
        response = client.get(reverse('get-put-delete-spending', kwargs={'id': 50}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewSpendingsTest(TestCase):
    def setUp(self):
        self.valid_payload = {
            "amount": 1000,
            "currency": "HUF",
            "description": "Food"
        }
        self.invalid_payload = {
            "amount": 500,
            "currency": "USDOLLAR",
            "description": "Rent"
        }

    def test_create_valid_spending(self):
        response = client.post(
            reverse('get-post-spending'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_spending(self):
        response = client.post(
            reverse('get-post-spending'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateOneSpendingsTest(TestCase):
    def setUp(self):
        self.huf_spending = Spending.objects.create(
            amount=1000, currency="HUF", description="Food"
        )
        self.valid_payload = {
            "amount": 2000,
            "currency": "HUF",
            "description": "Food"
        }
        self.invalid_payload = {
            "amount": 1000,
            "currency": "USADOLLAR",
            "description": ""
        }

    def test_valid_update_spending(self):
        response = client.put(
            reverse('get-put-delete-spending', kwargs={'id': self.huf_spending.pk}),
            data=json.dumps(self.valid_payload),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_spending(self):
        response = client.put(
            reverse('get-put-delete-spending', kwargs={'id': self.huf_spending.pk}),
            data=json.dumps(self.invalid_payload),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteOneSpendingsTest(TestCase):
    def setUp(self):
        self.huf_spending = Spending.objects.create(
            amount=1000, currency="HUF", description="Food"
        )
        self.usd_spending = Spending.objects.create(
            amount=500, currency="USD", description="Rent"
        )

    def test_valid_delete_spending(self):
        response = client.delete(
            reverse('get-put-delete-spending',
            kwargs={'id': self.huf_spending.pk})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_invalid_spending(self):
        response = client.delete(
            reverse('get-put-delete-spending',
            kwargs={'id': 50})
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
