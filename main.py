from pymongo import MongoClient




if __name__ == "__main__":
    print("start")
   # Connect to MongoDB
    client = MongoClient("mongodb://admin:pass@localhost:27017")  # Assuming MongoDB is running on localhost and default port 27017
    
    db = client['mydatabase']

    # Access a specific collection within the database
    collection = db['mycollection2']

    # Now you can perform operations on the collection, for example, inserting a document
    document = {'name': 'Sim', 'age': 27, "new_field": "fake_info", "object_field": {"first": 1, "second": 3, "third": {"first": 1, "second": 3}}}
    collection.insert_one(document)


    result = list(collection.find())
    print(result)  # This will print the document with name 'John'