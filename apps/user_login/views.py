from django.shortcuts import render, HttpResponse, redirect

def index(request):
	response = "Hello there"
	return HttpResponse(response)