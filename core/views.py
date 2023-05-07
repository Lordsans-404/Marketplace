from django.shortcuts import render
from userprofile.forms import *
from . import utils
from django.views.generic import (
	TemplateView,
	DetailView,
	)

# class HomePage(TemplateView):
# 	template_name = "core/frontpage.html"

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		print(context['view'])
# 		return context

# Create your views here.
def frontpage(request):
	print(request.user)
	if request.method == "POST":
		if not request.user.is_authenticated:
			if request.POST['submit'] == 'login':
				utils.loginUser(request)
			if request.POST['submit'] == 'signup':
				utils.signupUser(request)
	context = {
		'loginform':FormLogin,
		'signupform':FormRegister,
	}
	return render(request,"core/frontpage.html",context)