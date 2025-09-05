from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WrestlerViewSet
from . import views

router = DefaultRouter()
router.register(r'wrestlers', WrestlerViewSet)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
    path("", views.WrestlerList.as_view()),
]