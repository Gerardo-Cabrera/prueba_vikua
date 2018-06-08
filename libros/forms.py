# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from models import MyUser

# class CustomUserCreationForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super(CustomUserCreationForm, self).__init__(*args, **kwargs)
#         del self.fields['username']


# class CustomUserChangeForm(UserChangeForm):
#     def __init__(self, *args, **kwargs):
#         super(CustomUserChangeForm, self).__init__(*args, **kwargs)
#         del self.fields['username']

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )