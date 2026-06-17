from django.http import HttpResponse
from django.shortcuts import render

def about(request, username):
    return HttpResponse("<h1>about</h1>" + username)
