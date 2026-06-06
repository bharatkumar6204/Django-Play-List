from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def post_details(request,post_id):
    return HttpResponse(f"<h1>Show Blog Post {post_id}  </h1>")

def user_profile(request,username):
    return HttpResponse(f"<h1>Profile of User {username} </h1>")
