import pymongo
from decouple import config



try:
    client = pymongo.MongoClient(config('DJANGO_DB_HOST'))
    db = client['web-ai']
    print("Connected to MongoDB Atlas")
except pymongo.errors.ConnectionFailure as e:
    print(f"Failed to connect to MongoDB Atlas: {e}")
