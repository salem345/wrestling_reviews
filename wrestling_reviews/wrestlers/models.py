from django.db import models

class Wrestler(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    debut_year = models.IntegerField()

    def __str__(self):
        return self.name

# Create your models here.
