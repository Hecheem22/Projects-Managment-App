from Accounts.models import User
from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm



class LoginForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    class Meta:
        model = User
        fields = ['username' , 'password']


class AddUserForm(BSModalModelForm):
    class Meta:
        model = User
        fields = ['first_name' , 'last_name' , 'email' , 'Type']
