from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class CustUser(AbstractUser):
	avatar = models.ImageField(upload_to=("avatar-url/"),blank=True,null=True)
	about = models.CharField(max_length=50,default="Hello World!",blank=True)

	def __str__(self):
		return self.username

