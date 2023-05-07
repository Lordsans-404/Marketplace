from userprofile.forms import (FormLogin,FormRegister)
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect

# Login Utilitiy
def loginUser(request):
	req = request.POST
	form = FormLogin(req)
	username = req.get('username')
	password = req.get('password')
	user = authenticate(request,username=username,password=password)
	if not user or not user.is_active:
		messages.error(request,'username or password not correct')
	elif user: #if user exists
		login(request,user)
		messages.success(request,'Login Successed')

def signupUser(request):
	req = request.POST
	form = FormRegister(req)
	if form.is_valid():
		user2 = authenticate(request,username=req['username'],password=req['password1'])
		print(user2,'uhuy')
		user = form.save()
		login(request,user)
		messages.success(request,'Your Account Has Been Created')
	else:
		messages.error(request,'Failed To Create Account')
