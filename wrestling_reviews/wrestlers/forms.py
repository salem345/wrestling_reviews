from django import forms
from .models import Wrestler




class WrestlerForm(forms.ModelForm):
    class Meta:
        model = Wrestler
        fields = ['name', 'country', 'debut_year', 'birth_date', 'debut_date']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter wrestler name'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter country'
            }),
            'debut_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1900',
                'max': '2024',
                'placeholder': 'Enter debut year'
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'debut_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make required fields
        self.fields['name'].required = True
        self.fields['country'].required = True
        self.fields['debut_year'].required = True
