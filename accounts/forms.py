from django import forms
from . models import CustomUser


class UserModelForm(forms.ModelForm):
    username = forms.CharField(label='Please pick a username for yourself!',
                               widget=forms.TextInput(
                                 attrs={'placeholder': 'Pick your username!', 'class': 'form-control'}
                               ))
    email = forms.EmailField(label='Please pick a unique email!',
                               widget=forms.TextInput(
                                 attrs={'placeholder': 'Pick a unique email!', 'class': 'form-control'}
                               ))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput
                               )
    confirm_password = forms.CharField(label='Confirm Password',
                                           widget=forms.PasswordInput
                                           )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError('Password do not match!')
        return cd['confirm_password']


class SettingsForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email',]



