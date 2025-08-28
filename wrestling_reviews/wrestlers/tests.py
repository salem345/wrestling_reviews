from django.test import TestCase
from .models import Wrestler

class WrestlerModelTest(TestCase):
    def setUp(self):
        Wrestler.objects.create(name="The Rock", country="USA", birth_date="1972-05-02")

    def test_wrestler_name(self):
        wrestler = Wrestler.objects.get(name="The Rock")
        self.assertEqual(wrestler.name, "The Rock")


# Create your tests here.
