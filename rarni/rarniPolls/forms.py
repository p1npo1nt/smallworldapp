from django.forms import ModelForm
from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User #models the form after the User model and will store the values under the user Model
        fields = '__all__' #sets the values of the form to all values
