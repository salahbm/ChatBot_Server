import pymongo

try:
    client = pymongo.MongoClient('mongodb+srv://salahbm:Bahmuhsal2001@web-ai.qxrtmxa.mongodb.net/?retryWrites=true&w=majority')
    db = client['web-ai']

    if db is not None:
        print("Connected to MongoDB Atlas")

        # Perform your database operations here
        # For example, you can retrieve a document from a collection
        collection = db['your_collection_name']
        document = collection.find_one({'your_key': 'your_value'})
        print(document)

    else:
        print("Failed to get a reference to the database.")

except pymongo.errors.ConnectionFailure as e:
    print(f"Failed to connect to MongoDB Atlas: {e}")
