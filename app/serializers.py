from rest_framework import  serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'name', 'email', 'phone','marketingRequirement', 'desiredService','salesDepAgreement')


class ChatbotStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatbotSteps
        fields = '__all__'