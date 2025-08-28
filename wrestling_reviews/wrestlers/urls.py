from django.urls import path
from .views import WrestlerListCreateView, WrestlerDetailView

urlpatterns = [
    path('wrestlers/', WrestlerListCreateView.as_view(), name='wrestler-list-create'),
    path('wrestlers/<int:pk>/', WrestlerDetailView.as_view(), name='wrestler-detail'),
]