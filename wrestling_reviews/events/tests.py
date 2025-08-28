from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Event
from datetime import date

class EventTests(APITestCase):
    def test_list_events(self):
        Event.objects.create(name="WrestleMania 40", date=date(2024,4,7), location="Philadelphia", promotion="WWE")
        url = reverse("event-list")  # جاي من الـ router basename
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(res.json()), 1)
# Create your tests here.
