from django import forms
from .models import Review
from wrestlers.models import Wrestler
from events.models import Event


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['match_title', 'event', 'wrestlers', 'review_content', 'rating']
        widgets = {
            'match_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter match title (e.g., John Cena vs The Rock)'
            }),
            'event': forms.Select(attrs={
                'class': 'form-select'
            }),
            'wrestlers': forms.SelectMultiple(attrs={
                'class': 'form-select',
                'size': '6'
            }),
            'review_content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Write your detailed review here...'
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'max': '5',
                'step': '0.1',
                'placeholder': '0.0'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['event'].queryset = Event.objects.all().order_by('-date')
        self.fields['wrestlers'].queryset = Wrestler.objects.all().order_by('name')
        
        # Make fields required
        self.fields['match_title'].required = True
        self.fields['event'].required = True
        self.fields['wrestlers'].required = True
        self.fields['review_content'].required = True
        self.fields['rating'].required = True