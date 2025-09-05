from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reviews.views import ReviewViewSet, WrestlerViewSet
from django.contrib import admin
from . import views
router = DefaultRouter()
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'wrestlers', WrestlerViewSet, basename='wrestler')

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path("", views.WrestlerList.as_view()),
]