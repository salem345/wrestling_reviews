from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200)
    promotion = models.CharField(max_length=100, blank=True, default="")
    description = models.TextField(blank=True, default="")
    is_ppv = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Meta:
        ordering = ["-date", "-created_at"]

def __str__(self):
        return self.name

# Create your models here.
