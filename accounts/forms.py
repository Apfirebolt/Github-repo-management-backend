from django import forms
from . models import UserModel


class UserModelForm(forms.ModelForm):
    username = forms.CharField(label='Please pick a username for yourself!',
                               widget=forms.TextInput(
                                 attrs={'placeholder': 'Pick your username!', 'class': 'form-control'}
                               ))
    email = forms.EmailField(label='Please pick a unique email!',
                               widget=forms.TextInput(
                                 attrs={'placeholder': 'Pick a unique email!', 'class': 'form-control'}
                               ))
    first_name = forms.CharField(label='Your First Name is!',
                               widget=forms.TextInput(
                                 attrs={'placeholder': 'Enter your first name!', 'class': 'form-control'}
                               ))
    last_name = forms.CharField(label='Your last name is!',
                               widget=forms.TextInput(
                                 attrs={'placeholder': 'Enter your last name!', 'class': 'form-control'}
                               ))
    password = forms.PasswordInput()
    confirm_password = forms.PasswordInput()

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'first_name', 'last_name', 'password']


