"""
URL configuration for wrestling_reviews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reviews.views import ReviewViewSet, WrestlerViewSet
from events.views import EventViewSet
from users.views import UserViewSet
from . import views
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'wrestlers', WrestlerViewSet, basename='wrestler')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'events', EventViewSet, basename='event')
router.register(r'users', UserViewSet, basename='user')





urlpatterns = [
    path("admin/", admin.site.urls),

    # Web interface URLs
    path('', views.home, name='home'),
    path('reviews/', views.reviews_list, name='reviews_list'),
    path('reviews/<int:pk>/', views.review_detail, name='review_detail'),
    path('reviews/add/', views.add_review, name='add_review'),
    path('reviews/<int:pk>/edit/', views.edit_review, name='edit_review'),
    path('reviews/<int:pk>/delete/', views.delete_review, name='delete_review'),

    path('wrestlers/', views.wrestlers_list, name='wrestlers_list'),
    path('wrestlers/<int:pk>/', views.wrestler_detail, name='wrestler_detail'),
    path('wrestlers/add/', views.add_wrestler, name='add_wrestler'),
    path('wrestlers/<int:pk>/edit/', views.edit_wrestler, name='edit_wrestler'),

    path('events/', views.events_list, name='events_list'),
    path('events/<int:pk>/', views.event_detail, name='event_detail'),
    path('events/add/', views.add_event, name='add_event'),
    path('events/<int:pk>/edit/', views.edit_event, name='edit_event'),

    # API URLs
    path("api/", include("wrestling_reviews.api_urls")),
    path("api/wrestlers/", include("wrestlers.urls")),
    path("api/events/", include("events.urls")),
    path("api/reviews/", include("reviews.urls")),
    path("api/users/", include("users.urls")),

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Main site URLs
    path('', views.home, name='home'),

    # Reviews URLs
    path('reviews/', views.reviews_list, name='reviews_list'),
    path('reviews/<int:pk>/', views.review_detail, name='review_detail'),
    path('reviews/add/', views.add_review, name='add_review'),
    path('reviews/<int:pk>/edit/', views.edit_review, name='edit_review'),
    path('reviews/<int:pk>/delete/', views.delete_review, name='delete_review'),

    # Wrestlers URLs
    path('wrestlers/', views.wrestlers_list, name='wrestlers_list'),
    path('wrestlers/<int:pk>/', views.wrestler_detail, name='wrestler_detail'),
    path('wrestlers/add/', views.add_wrestler, name='add_wrestler'),
    path('wrestlers/<int:pk>/edit/', views.edit_wrestler, name='edit_wrestler'),
    path('wrestlers/<int:pk>/delete/', views.delete_wrestler, name='delete_wrestler'),

    # Events URLs
    path('events/', views.events_list, name='events_list'),
    path('events/<int:pk>/', views.event_detail, name='event_detail'),
    path('events/add/', views.add_event, name='add_event'),
    path('events/<int:pk>/edit/', views.edit_event, name='edit_event'),
    path('events/<int:pk>/delete/', views.delete_event, name='delete_event'),
]