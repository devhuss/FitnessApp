from django import forms
from .models import Workout, Contact

INTENSITY_CHOICES = (
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
)


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['workout', 'intensity', 'total_sets', 'duration', 'bodyweight', 'date']

        widgets = {
            'workout': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Example: Chest, Lower Body, Pull, etc.'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter duration in minutes'}),
            'intensity': forms.Select(choices=INTENSITY_CHOICES),
            'date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'mm/dd/yy'}),
            'created_at': forms.TextInput(attrs={'class': 'form-control'}),
            'bodyweight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter bodyweight in lbs'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example: abc@123.com'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
