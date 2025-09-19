@@ .. @@
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
+from django.contrib.auth.decorators import login_required, user_passes_test
+from django.contrib.admin.views.decorators import staff_member_required
from reviews.models import Review
from reviews.forms import ReviewForm
from wrestlers.models import Wrestler
from wrestlers.forms import WrestlerForm
from events.models import Event
from events.forms import EventForm
from users.models import User

+def is_superuser(user):
+    return user.is_superuser
+
+def is_staff_or_superuser(user):
+    return user.is_staff or user.is_superuser

def home(request):
    # Get latest reviews
    latest_reviews = Review.objects.select_related('event', 'user').prefetch_related('wrestlers').order_by('-created_at')[:6]
    
    # Get some stats
    total_reviews = Review.objects.count()
    total_wrestlers = Wrestler.objects.count()
    total_events = Event.objects.count()
    
    # Get top wrestlers (most reviewed)
    top_wrestlers = Wrestler.objects.prefetch_related('reviews').all()[:5]
    
    context = {
        'latest_reviews': latest_reviews,
        'total_reviews': total_reviews,
        'total_wrestlers': total_wrestlers,
        'total_events': total_events,
        'top_wrestlers': top_wrestlers,
    }
    return render(request, 'home.html', context)

def reviews_list(request):
    reviews = Review.objects.select_related('event', 'user').prefetch_related('wrestlers').order_by('-created_at')
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        reviews = reviews.filter(
            Q(match_title__icontains=search_query) |
            Q(review_content__icontains=search_query) |
            Q(event__name__icontains=search_query) |
            Q(wrestlers__name__icontains=search_query)
        ).distinct()
    
    # Pagination
    paginator = Paginator(reviews, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'reviews/list.html', context)

def review_detail(request, pk):
    review = get_object_or_404(Review.objects.select_related('event', 'user').prefetch_related('wrestlers'), pk=pk)
    context = {'review': review}
    return render(request, 'reviews/detail.html', context)

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            
            # Assign user - create default admin if no users exist
            if not User.objects.exists():
                user = User.objects.create_user(
                    username='admin',
                    email='admin@wrestlingreviews.com',
                    password='admin123',
                    is_staff=True,
                    is_superuser=True
                )
            else:
                user = User.objects.first()
            
            review.user = user
            review.save()
            form.save_m2m()  # Save many-to-many relationships
            messages.success(request, 'Review added successfully!')
            return redirect('review_detail', pk=review.pk)
    else:
        form = ReviewForm()
    
    context = {'form': form, 'title': 'Add Review'}
    return render(request, 'reviews/form.html', context)

def edit_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review updated successfully!')
            return redirect('review_detail', pk=review.pk)
    else:
        form = ReviewForm(instance=review)
    
    context = {'form': form, 'title': 'Edit Review', 'review': review}
    return render(request, 'reviews/form.html', context)

def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Review deleted successfully!')
        return redirect('reviews_list')
    
    context = {'review': review}
    return render(request, 'reviews/confirm_delete.html', context)

# Wrestlers Views
def wrestlers_list(request):
    wrestlers = Wrestler.objects.all().order_by('name')
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        wrestlers = wrestlers.filter(name__icontains=search_query)
    
    # Pagination
    paginator = Paginator(wrestlers, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'wrestlers/list.html', context)

def wrestler_detail(request, pk):
    wrestler = get_object_or_404(Wrestler.objects.prefetch_related('reviews__event'), pk=pk)
    reviews = wrestler.reviews.all().order_by('-created_at')
    
    context = {
        'wrestler': wrestler,
        'reviews': reviews,
    }
    return render(request, 'wrestlers/detail.html', context)

+@user_passes_test(is_superuser)
def add_wrestler(request):
    if request.method == 'POST':
        form = WrestlerForm(request.POST)
        if form.is_valid():
            wrestler = form.save()
            messages.success(request, 'Wrestler added successfully!')
            return redirect('wrestler_detail', pk=wrestler.pk)
    else:
        form = WrestlerForm()
    
    context = {'form': form, 'title': 'Add Wrestler'}
    return render(request, 'wrestlers/form.html', context)

+@user_passes_test(is_superuser)
def edit_wrestler(request, pk):
    wrestler = get_object_or_404(Wrestler, pk=pk)
    if request.method == 'POST':
        form = WrestlerForm(request.POST, instance=wrestler)
        if form.is_valid():
            form.save()
            messages.success(request, 'Wrestler updated successfully!')
            return redirect('wrestler_detail', pk=wrestler.pk)
    else:
        form = WrestlerForm(instance=wrestler)
    
    context = {'form': form, 'title': 'Edit Wrestler', 'wrestler': wrestler}
    return render(request, 'wrestlers/form.html', context)

+@user_passes_test(is_superuser)
+def delete_wrestler(request, pk):
+    wrestler = get_object_or_404(Wrestler, pk=pk)
+    if request.method == 'POST':
+        wrestler.delete()
+        messages.success(request, 'Wrestler deleted successfully!')
+        return redirect('wrestlers_list')
+    
+    context = {'wrestler': wrestler}
+    return render(request, 'wrestlers/confirm_delete.html', context)

# Events Views
def events_list(request):
    events = Event.objects.all().order_by('-date')
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        events = events.filter(
            Q(name__icontains=search_query) |
            Q(location__icontains=search_query) |
            Q(promotion__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(events, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'events/list.html', context)

def event_detail(request, pk):
    event = get_object_or_404(Event.objects.prefetch_related('reviews__wrestlers', 'reviews__user'), pk=pk)
    reviews = event.reviews.all().order_by('-created_at')
    
    context = {
        'event': event,
        'reviews': reviews,
    }
    return render(request, 'events/detail.html', context)

+@user_passes_test(is_superuser)
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            messages.success(request, 'Event added successfully!')
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm()
    
    context = {'form': form, 'title': 'Add Event'}
    return render(request, 'events/form.html', context)

+@user_passes_test(is_superuser)
def edit_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    
    context = {'form': form, 'title': 'Edit Event', 'event': event}
    return render(request, 'events/form.html', context)

+@user_passes_test(is_superuser)
+def delete_event(request, pk):
+    event = get_object_or_404(Event, pk=pk)
+    if request.method == 'POST':
+        event.delete()
+        messages.success(request, 'Event deleted successfully!')
+        return redirect('events_list')
+    
+    context = {'event': event}
+    return render(request, 'events/confirm_delete.html', context)