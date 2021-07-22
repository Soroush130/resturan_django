from django import forms
from .models import Reseve


class ResevationForm(forms.ModelForm):
    class Meta:
        model = Reseve
        fields = '__all__'
