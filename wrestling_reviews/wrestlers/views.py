from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Wrestler
from .serializers import WrestlerSerializer

class WrestlerListCreateView(generics.ListCreateAPIView):
    queryset = Wrestler.objects.all()
    serializer_class = WrestlerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class WrestlerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wrestler.objects.all()
    serializer_class = WrestlerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Create your views here.
