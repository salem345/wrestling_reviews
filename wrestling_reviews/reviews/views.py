from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer
from wrestlers.models import Wrestler
from wrestlers.serializers import WrestlerSerializer


class WrestlerViewSet(viewsets.ModelViewSet):
    queryset = Wrestler.objects.all()
    serializer_class = WrestlerSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by("-created_at")
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]

    # هنا بتخصص POST (create)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)