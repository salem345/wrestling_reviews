from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WrestlerViewSet

router = DefaultRouter()
router.register(r'wrestlers', WrestlerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

router = DefaultRouter()
router.register(r"", ReviewViewSet)

urlpatterns = router.urls