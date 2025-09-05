from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'location', 'promotion', 'description', 'is_ppv']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter event name'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter location'
            }),
            'promotion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter promotion (e.g., WWE, AEW)'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter event description (optional)'
            }),
            'is_ppv': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }

    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make required fields
        self.fields['name'].required = True
        self.fields['date'].required = True
        self.fields['location'].required = True
