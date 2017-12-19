from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),

	#GET request to /users
	url(r'^users$', views.index),

	#GET request to users/<id>
	url(r'^users/(?P<user_id>\d+)$', views.show),

	#GET request to users/new - form to create new user
	url(r'^users/new$', views.new),

	#GET request to users/<id>/edit - form to edit existing user w/ given id
	url(r'^users/(?P<user_id>\d+)/edit$', views.edit),

	#POST to /users/create - calls create method - insert new user into database.
	#POST should be sent from form on page to /users/new - redirect to /users/<id>
	url(r'^users/create$', views.create),

	#POST to /users/update - calls update method to process submitted form sent
	#from /users/<id>/edit - redirect to /users/<id> once updated
	url(r'^users/(?P<user_id>\d+)/update$', views.update),

	url(r'^users/(?P<user_id>\d+)/destroy$', views.destroy)
]