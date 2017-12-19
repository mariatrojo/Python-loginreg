from django.shortcuts import render, HttpResponse, redirect

def index(request):
	response = "Hello hi"
	return HttpResponse(response)