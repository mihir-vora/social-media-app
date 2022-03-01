from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Feedback


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
                'class' : 'form-group form-control ',
                # 'placeholder' : 'Username',
            })
        self.fields['email'].widget.attrs.update({
                'class' : 'form-group form-control ',
                # 'placeholder' : 'Email',
            })
        self.fields['password1'].widget.attrs.update({
                'class' : 'form-group form-control ',
                # 'placeholder' : 'Password',
            })
        self.fields['password2'].widget.attrs.update({
                'class' : 'form-group form-control ',
                # 'placeholder' : 'Confirm Password',
               
        })
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
      


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio',]

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['subject', 'message']

    
