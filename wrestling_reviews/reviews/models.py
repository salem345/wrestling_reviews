from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from events.models import Event
from wrestlers.models import Wrestler

class Review(models.Model):
    match_title = models.CharField(max_length=200)
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="reviews")
    wrestlers = models.ManyToManyField(Wrestler, related_name="reviews")
    review_content = models.TextField()
    rating = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.match_title} - {self.rating}/5"

# Create your models here.
