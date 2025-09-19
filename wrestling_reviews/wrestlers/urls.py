from .views import WrestlerListCreateView, WrestlerDetailView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WrestlerViewSet


router = DefaultRouter()
router.register(r'wrestlers', WrestlerViewSet)

urlpatterns = [
    path('', WrestlerListCreateView.as_view(), name='wrestler-list-create'),
    path('<int:pk>/', WrestlerDetailView.as_view(), name='wrestler-detail'),
    path('', include(router.urls)),
]

router = DefaultRouter()
router.register(r'', WrestlerViewSet, basename='wrestler')
urlpatterns = router.urls