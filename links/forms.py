from django import forms
from .models import Link

class LinkForm(forms.ModelForm):
    # due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Link
        fields = ['name', 'url']
        
