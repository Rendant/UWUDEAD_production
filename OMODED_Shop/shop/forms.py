from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': ' Email'}))

    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': ' Username'}),
            'email': forms.TextInput(attrs={'placeholder': ' Email'}),
        }
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': ' Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': ' Password confirmation'})

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': ' Username'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': ' Password'})


class ResetForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super(ResetForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': ' Email'})
