from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, WrestlerViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'wrestlers', WrestlerViewSet)
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]
