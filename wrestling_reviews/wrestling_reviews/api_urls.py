from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reviews.views import ReviewViewSet
from wrestlers.views import WrestlerViewSet
from users.views import UserViewSet

urlpatterns = [
    path('wrestlers/', include('wrestlers.urls')),
    path('events/', include('events.urls')),
    path('reviews/', include('reviews.urls')),
    path('users/', include('users.urls')),
]