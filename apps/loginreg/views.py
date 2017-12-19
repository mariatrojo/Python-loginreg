from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import * 

def index(request):
	return render(request, "loginreg/index.html")
 
def success(request):
	try:
		id = request.session['user_id']
		user = User.objects.get(id = id)
		# do cody things like get data n stuff
		context = { "user": User.objects.get(id = request.session["user_id"])}
		return render(request, "loginreg/success.html", context)
	except:
		return redirect('/')

def register(request):
	result = User.objects.register_validator(request.POST)
	if type(result) == list:
		for error in result:
			messages.error(request, error)
		return redirect('/')
	else:
		request.session['user_id'] = result.id
		messages.success(request, "Successfully registered!")
		return redirect('/success')

def login(request):
	result = User.objects.login_validator(request.POST)
	if type(result) == list:
		for error in result:
			messages.error(request, error)
		return redirect('/')
	else:
		request.session['user_id'] = result.id
		messages.success(request, "Successfully logged in!")
		return redirect('/success')

def logout(request):
	request.session.clear()
	return redirect('/')