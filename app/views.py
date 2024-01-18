from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from . serializer import *
from rest_framework.response import Response


# Create the USER API View

class UserView(APIView):
    def get(self, request):
        output = [{'username': output.username, 'password': output.password} for output in User.objects.all()]
        return Response(output)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,)