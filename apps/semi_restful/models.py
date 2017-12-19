from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class BlogManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['first_name']) < 1:
			errors["first_name"] = "First name cannot be empty"
		if len(postData['last_name']) < 1:
			errors["desc"] = "Last name cannot be empty"
		if len(postData['email']) < 1:
			errors["email"] = "Email cannot be empty"
		elif not EMAIL_REGEX.match(postData['email']):
			errors["email"] = "Invalid Email!"
	
		try:
			User.objects.get(email=postData['email'])
			errors["email"] = "Email is already used"
		except:
			pass

		return errors
	
	def update_validator(self, postData):
		errors = {}
		if len(postData['first_name']) < 1:
			errors["first_name"] = "First name cannot be empty"
		if len(postData['last_name']) < 1:
			errors["desc"] = "Last name cannot be empty"
		if len(postData['email']) < 1:
			errors["email"] = "Email cannot be empty"
		elif not EMAIL_REGEX.match(postData['email']):
			errors["email"] = "Invalid Email!"

		return errors

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = BlogManager()