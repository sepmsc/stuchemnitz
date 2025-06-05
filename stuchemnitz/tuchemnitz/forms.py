from django import forms
from tuchemnitz.models import Comments, Reply
from django.contrib.auth.models import User

class SubmitForm(forms.Form):
    class Meta:
        fields = ['__all__']
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    comment = forms.CharField(widget=forms.Textarea, required=True)
    reply = forms.CharField(widget=forms.Textarea, required=False)
    created_at = forms.DateTimeField(auto_now_add=True, required=False)

class AdminSignupForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_staff = True

        if commit:
            user.save()
        return user


    