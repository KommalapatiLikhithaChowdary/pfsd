from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'company']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }
