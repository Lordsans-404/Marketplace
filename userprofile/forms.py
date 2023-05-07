from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CustomUserForm(UserCreationForm):
	class Meta:
		model = CustUser
		fields = '__all__'

# Form For Login And Sign Up

class FormLogin(forms.ModelForm):
	class Meta:
		model = CustUser
		fields = [
			'username',
			'password'
		]
		help_texts = {
			'username':None,
		}
		widgets = {
			'password':forms.TextInput(
				attrs = {
					'type':'password'
				}
			)
		}

class FormRegister(forms.ModelForm):
	password1 = forms.CharField(
		label=('Password'),
		strip=False,
		widget=forms.PasswordInput(),
	)

	password2 = forms.CharField(
		label=("Password confirmation"),
		strip=False,
		help_text=("Enter the same password as before, for verification."),
		widget=forms.PasswordInput(),

	)
	class Meta:
		model = CustUser
		fields = [
			'username',
			'email',
			'password1',
			'password2',
		]
		help_texts = {
            'username': None,
        }

