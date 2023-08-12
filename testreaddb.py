from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://SIC4:SIC4Password@cluster0.vp0fgmb.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client['MyDatabase'] # ganti sesuai dengan nama database kalian
my_collections = db['MyCollection'] # ganti sesuai dengan nama collections kalian

for my_collection in my_collections.find():
  print(my_collection.get('nama'))
  print(my_collection.get('Jurusan'))
  print(my_collection.get('Nilai'))
