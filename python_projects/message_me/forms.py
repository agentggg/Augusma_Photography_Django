from django import forms
from .models import identity

class identity(forms.ModelForm):
    class Meta:
        model = identity
        fields = "__all__"
