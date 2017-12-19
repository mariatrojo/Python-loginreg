from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class BlogManager(models.Manager):
	def register_validator(self, postData):
		errors = []

		first_name = postData['first_name']
		last_name = postData['last_name']
		email = postData['email']
		password = postData['password']
		conf_password = postData['confirm_password']

		if not first_name:
			errors.append("First name cannot be empty")
		elif len(first_name) < 2:
			errors.append("First name must be longer than 1 character")
		elif not first_name.isalpha():
			errors.append("First name can only contain letters")

		if not last_name:
			errors.append("Last name cannot be empty")
		elif len(last_name) < 2:
			errors.append("Last name must be longer than 1 character")
		elif not last_name.isalpha():
			errors.append("Last name can only contain letters")

		if not email:
			errors.append("Email cannot be empty")
		elif not EMAIL_REGEX.match(email):
			errors.append("Invalid Email!")

		if len(password) < 1:
			errors.append("Password cannot be empty")
		elif len(password) < 8:
			errors.append("Password must be 8 characters or longer")
		elif password != conf_password:
			errors.append("Passwords don't match")

		if not errors:
			try:
				User.objects.get(email=email)
				errors.append("Email is already used")
			except:
				hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
				return User.objects.create(first_name=first_name, last_name=last_name, email=email, password=hash)

		return errors

	def login_validator(self, postData):
		errors = []
		email = postData['email']
		password = postData['password']

		if not email:
			errors.append("Email cannot be empty")
		elif not EMAIL_REGEX.match(email):
			errors.append("Invalid Email!")
		
		if not password:
			errors.append("Password cannot be empty")
		elif len(password) < 8:
			errors.append("Password must be 8 characters or longer")

		if not errors:
			try:
				user = User.objects.get(email=email)
				if bcrypt.checkpw(password.encode(), user.password.encode()):
					return user
			except:
				errors.append("You aren't registered yet")

		return errors
	

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = BlogManager()