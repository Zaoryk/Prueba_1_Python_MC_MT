from django import forms
from .models import Organization

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Organization
        fields = ["name", "email", "password"]

    def save(self, commit=True):
        org = super().save(commit=False)
        org.set_password(self.cleaned_data["password"])
        if commit:
            org.save()
        return org
    
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class PasswordResetForm(forms.Form):
    email = forms.EmailField()
