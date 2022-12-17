from django.forms import ModelForm, forms
from django import forms
from .models import User, Email
from django.forms import TextInput, EmailInput

from django.conf import settings

class UserForm(ModelForm):
    class Meta:
        model = User #models the form after the User model and will store the values under the user Model
        fields = '__all__' #sets the values of the form to all values

class EmailForm(ModelForm):
    class Meta:
        model = Email #models the form after the User model and will store the values under the user Model
        fields = '__all__' #sets the values of the form to all values
        widgets = {
            'email': EmailInput(attrs={
                'class': "input-lg half bw-0 fw-300 bg-indigo-lightest-10 white ph-indigo-lightest focus-white opacity-80 fs-s3 py-5 min-w-25vw br-r-0", 
                'placeholder': 'Email'
                })
        }