from django.shortcuts import render, HttpResponse, redirect

def index(request):
	response = "Hello"
	return HttpResponse(response)