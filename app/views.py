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

class userResponse(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Serializer Errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ChatbotStepListCreateView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = ChatbotSteps.objects.all()
        serializer = ChatbotStepSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data

        if isinstance(data, list):
            serializer_list = [ChatbotStepSerializer(data=item) for item in data]
            valid = all([serializer.is_valid() for serializer in serializer_list])

            if valid:
                instances = [serializer.save() for serializer in serializer_list]
                return Response(ChatbotStepSerializer(instances, many=True).data, status=status.HTTP_201_CREATED)
            else:
                errors = [serializer.errors for serializer in serializer_list]
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = ChatbotStepSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





def get_user_by_id(request):
    email = request.data.get('email')
    records=user_collection.find_one({'email':email})
    return HttpResponse(records)
