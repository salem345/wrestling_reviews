from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from .views import WrestlerViewSet

router = DefaultRouter()
router.register(r'wrestlers', WrestlerViewSet)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
]