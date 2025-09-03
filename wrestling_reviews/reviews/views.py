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


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def post(self, request, *args, **kwargs):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            permissions = [IsAdminUser]
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request, *args, **kwargs):
        review = get_object_or_404(Review, pk=kwargs['pk'])
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    def put(self, request, *args, **kwargs):
        review = get_object_or_404(Review, pk=kwargs['pk'])
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            permissions = [IsAdminUser]
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def patch(self, request, *args, **kwargs):
        review = get_object_or_404(Review, pk=kwargs['pk'])
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            permissions = [IsAdminUser]
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, *args, **kwargs):
        review = get_object_or_404(Review, pk=kwargs['pk'])
        review.delete()
        permissions = [IsAdminUser]
        return Response(status=204)
class WrestlerViewSet(viewsets.ModelViewSet):
    queryset = Wrestler.objects.all()
    serializer_class = WrestlerSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by("-created_at")
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Create your views here.
