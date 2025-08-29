from django.urls import path
from .views import WrestlerListCreateView, WrestlerDetailView

urlpatterns = [
    path('', WrestlerListCreateView.as_view(), name='wrestler-list-create'),
    path('<int:pk>/', WrestlerDetailView.as_view(), name='wrestler-detail'),
]