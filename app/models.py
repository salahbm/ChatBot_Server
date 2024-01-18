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