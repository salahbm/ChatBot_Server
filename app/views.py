from django.shortcuts import render
from rest_framework.views import APIView
from . models import user_collection
from . serializer import *
from rest_framework.response import Response
from django.http import HttpResponse


# Create the USER API View

def index(request):
    return HttpResponse('<h1>Hello, App is running!</h1>')

# store the user
def store_user(request):
    records={
        'username':"JOHN DOE",
        'password': '123456'
    }
    user_collection.insert_one(records)
    return HttpResponse('User added successfully')
# get user by id
def get_user_by_id(request):
    records=user_collection.find_one({'username':"JOHN DOE"})
    return HttpResponse(records)