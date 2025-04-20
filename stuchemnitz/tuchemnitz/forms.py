from django import forms
from tuchemnitz.models import Comments, Reply

class SubmitForm(forms.Form):
    class Meta:
        fields = ['__all__']
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    comment = forms.CharField(widget=forms.Textarea, required=True)
    reply = forms.CharField(widget=forms.Textarea, required=False)
    created_at = forms.DateTimeField(auto_now_add=True, required=False)
    