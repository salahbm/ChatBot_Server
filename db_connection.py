import pymongo



try:
    client = pymongo.MongoClient('mongodb+srv://salahbm:Bahmuhsal2001@web-ai.qxrtmxa.mongodb.net/?retryWrites=true&w=majority')
    db = client['web-ai']
    print("Connected to MongoDB Atlas")
except pymongo.errors.ConnectionFailure as e:
    print(f"Failed to connect to MongoDB Atlas: {e}")
