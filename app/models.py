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


chatbot_collection = db['Chatbot']
class ChatbotStep(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    message = models.TextField()
    user = models.BooleanField(default=False)
    trigger = models.CharField(max_length=255)
    validator = models.TextField(blank=True, null=True)
    options = models.JSONField(blank=True, null=True)
    end = models.BooleanField(default=False)


