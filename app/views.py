from django.shortcuts import render
from rest_framework.views import APIView
from . models import user_collection
from .serializers import *
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
import json
import bcrypt
from rest_framework import status



# Create the USER API View

def index(request):
    return HttpResponse('<h1>Hello, App is running!</h1>')

# store the user

class UserRegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({'error': 'Both email and password are required'}, status=status.HTTP_400_BAD_REQUEST)


        user_data = {'email': email, 'password': password}
        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Serializer Errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # get user by id
def get_user_by_id(request):
    email = request.data.get('email')
    records=user_collection.find_one({'email':email})
    return HttpResponse(records)
