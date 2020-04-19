from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    v_id = forms.CharField(max_length=10,label='Vehicle number')

    class Meta:
        model = User
        fields = ['username','email','v_id','password1','password2']

    '''def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        birthday = cleaned_data.get('birthday')
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')
        password = cleaned_data.get('password')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')'''
