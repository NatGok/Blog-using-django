from .models import CollaborateRequest
from django import forms

class CollaborateForm(forms.ModelForm):
    """
    Allow any user to send a collaboration request.
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
