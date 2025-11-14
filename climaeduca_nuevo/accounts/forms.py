from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    comuna = forms.CharField(max_length=100, required=True)
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'comuna', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.comuna = self.cleaned_data['comuna']
        if commit:
            user.save()
        return user