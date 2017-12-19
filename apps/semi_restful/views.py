from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import * 
 
#GET request to /users
def index(request):
	context = {"users": User.objects.all()}
	return render(request, 'semi_restful/index.html', context)

#GET request to /users/<id>
def show(request, user_id):
	context = {"users": User.objects.get(id = user_id)}
	return render(request, 'semi_restful/show_user.html', context)

#GET request to /users/new - form to create new user
def new(request):
	return render(request, 'semi_restful/new_user.html')

#GET request to /users/<id>/edit - form to edit existing user w/ given id
def edit(request, user_id):
	context = {"users": User.objects.get(id = user_id)}
	return render(request, 'semi_restful/edit_user.html', context)

#POST to /users/create - calls create method - insert new user into database.
#POST should be sent from form on page to /users/new - redirect to /users/<id>
def create(request):
	errors = User.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/users/new')
	else:
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		User.objects.create(first_name=first_name, last_name=last_name, email=email)
	return redirect('/users')

#GET to /users/<id>/destroy - calls destroy method to remove particular user
# w/ given id. redirect to /users
def destroy(request, user_id):
	User.objects.get(id=user_id).delete()
	return redirect('/users')

#POST to /users/update - calls update method to process submitted form sent
#from /users/<id>/edit - redirect to /users/<id> once updated
def update(request, user_id):
	errors = User.objects.update_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/users/'+user_id+'/edit')
	else:
		user = User.objects.get(id = user_id)
		user.first_name = request.POST['first_name']
		user.last_name = request.POST['last_name']
		user.email = request.POST['email']
		user.save()
	return redirect('/users/'+user_id)