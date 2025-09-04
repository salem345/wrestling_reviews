from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, permissions
from .models import Review
from .serializers import ReviewSerializer
from rest_framework import viewsets
from .models import Wrestler
from wrestlers.serializers import WrestlerSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404


class WrestlerViewSet(viewsets.ModelViewSet):
    queryset = Wrestler.objects.all()
    serializer_class = WrestlerSerializer



        
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
# Create your views here.
