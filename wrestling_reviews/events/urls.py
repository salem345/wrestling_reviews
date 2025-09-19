from rest_framework.routers import DefaultRouter
from .views import EventViewSet
from django.urls import path, include
from .views import WrestlerViewSet
from .views import EventList

router = DefaultRouter()
router.register(r'wrestlers', WrestlerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("", EventList.as_view()),
]

router = DefaultRouter()
router.register(r"", EventViewSet, basename="event")

urlpatterns = router.urls