from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Wrestler
from .serializers import WrestlerSerializer
from rest_framework import filters

class WrestlerListCreateView(generics.ListCreateAPIView):
    queryset = Wrestler.objects.all()
    serializer_class = WrestlerSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'bio']
    ordering_fields = ['debut_date']

class WrestlerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wrestler.objects.all()
    serializer_class = WrestlerSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'bio']
    ordering_fields = ['debut_date']

# Create your views here.
