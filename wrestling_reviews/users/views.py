from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from wrestlers.models import Wrestler
from wrestlers.serializers import WrestlerSerializer

class WrestlerViewSet(viewsets.ModelViewSet):
    queryset = Wrestler.objects.all()
    serializer_class = WrestlerSerializer

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]