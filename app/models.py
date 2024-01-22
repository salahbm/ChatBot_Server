from django.db import models
from db_connection import db

# User model


user_collection = db['Users']
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    marketingRequirement=models.CharField(max_length=255)
    desiredService=models.CharField(max_length=255)
    salesDepAgreement=models.CharField(max_length=255)


chatbot_collection = db['Chatbots']
class ChatbotSteps(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    message = models.TextField( null=True)
    user = models.BooleanField(default=False, null=True)
    trigger = models.CharField(max_length=255, null=True)
    validator = models.BooleanField(default=False, null=True)
    options = models.JSONField(blank=True, null=True)
    end = models.BooleanField(default=False, null=True)


