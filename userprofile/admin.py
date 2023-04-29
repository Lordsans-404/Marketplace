from django.contrib import admin
from .models import *
from .forms import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
	model = CustUser
	add_form = CustomUserForm
	# tell django admin there are new fields in User table
	fieldsets = *UserAdmin.fieldsets,(
		('Extra',{'fields':('avatar','about',)})
	)

admin.site.register(CustUser,CustomUserAdmin)	