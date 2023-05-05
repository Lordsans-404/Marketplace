from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CustomUserForm(UserCreationForm):
	class Meta:
		model = CustUser
		fields = '__all__'
