from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Event
from .serializers import EventSerializer
from wrestlers.models import Wrestler
from wrestlers.serializers import WrestlerSerializer
from rest_framework.generics import ListCreateAPIView

class EventList(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    """
    CRUD كامل للأحداث:
    - GET /api/events/        -> list
    - POST /api/events/       -> create
    - GET /api/events/<id>/   -> retrieve
    - PUT/PATCH /api/events/<id>/ -> update
    - DELETE /api/events/<id>/    -> destroy

    البحث/الترتيب/الفلاتر متاحة عبر DRF:
    - ?search=mania
    - ?ordering=date  أو ?ordering=-date
    - ?date__gte=2024-01-01&date__lte=2024-12-31
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # الفلاتر والبحث والترتيب
    filterset_fields = {
        "date": ["exact", "gte", "lte"],
        "promotion": ["exact", "icontains"],
        "is_ppv": ["exact"],
        "location": ["exact", "icontains"],
        "name": ["exact", "icontains"],
    }
    search_fields = ["name", "location", "promotion", "description"]
    ordering_fields = ["date", "created_at", "updated_at", "name"]
    ordering = ["-date"]


class WrestlerViewSet(viewsets.ModelViewSet):
    queryset = Wrestler.objects.all()
    serializer_class = WrestlerSerializer
# Create your views here.
