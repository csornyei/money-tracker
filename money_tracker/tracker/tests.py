from django.test import TestCase
from tracker.models import Spending

# Create your tests here.
class SpendingTestCase(TestCase):
    def setUp(self):
        Spending.objects.create(
            amount=1000,
            currency='HUF',
            description='food'
        )

    def test_spending_str(self):
        huf_spending = Spending.objects.get(amount=1000, currency='HUF')
        self.assertEqual(
            huf_spending.__str__(), "1000 HUF spent on food"
        )