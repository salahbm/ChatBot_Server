from django.db import models
from db_connection import db

# User model


user_collection = db['Users']
class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)