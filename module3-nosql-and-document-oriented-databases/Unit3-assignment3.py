import pymongo

connection_uri = "mongodb+srv://Ash827:<password>@cluster0-adjlc.mongodb.net/test?retryWrites=true&w=majority"
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("Client", type(client), client)

db = client.test
print("DB:", type(db))