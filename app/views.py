from django.shortcuts import render
from rest_framework.views import APIView
from . models import user_collection
from . serializer import *
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
import json
import bcrypt


# Create the USER API View

def index(request):
    return HttpResponse('<h1>Hello, App is running!</h1>')

# store the user


def store_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username', '')
            password = data.get('password', '')

            # Hash the password
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            # Perform validation and store data in the database
            records = {
                'username': username,
                'password': hashed_password.decode('utf-8')  # Store the hashed password in the database
            }
            user_collection.insert_one(records)

            return JsonResponse({'message': 'User added successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

# get user by id
def get_user_by_id(request):
    records=user_collection.find_one({'username':"JOHN DOE"})
    return HttpResponse(records)