from rest_framework import generics, permissions
from .models import Wrestler
from .serializers import WrestlerSerializer
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView

class WrestlerUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        wrestler = get_object_or_404(Wrestler, pk=kwargs['pk'])
        serializer = WrestlerSerializer(wrestler)
        return Response(serializer.data)
    def put(self, request, *args, **kwargs):
        wrestler = get_object_or_404(Wrestler, pk=kwargs['pk'])
        serializer = WrestlerSerializer(wrestler, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def patch(self, request, *args, **kwargs):
        wrestler = get_object_or_404(Wrestler, pk=kwargs['pk'])
        serializer = WrestlerSerializer(wrestler, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        wrestler = get_object_or_404(Wrestler, pk=kwargs['pk'])
        wrestler.delete()
        return Response(status=204)

class WrestlerViewSet(viewsets.ModelViewSet):
    queryset = Wrestler.objects.all()
    serializer_class = WrestlerSerializer

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
