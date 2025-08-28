from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from django.urls import path
from .views import UserListCreateView, UserDetailView

router = DefaultRouter()
router.register(r"", UserViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list-create'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]