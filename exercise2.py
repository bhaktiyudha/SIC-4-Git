from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask, request, jsonify

uri = "mongodb+srv://SIC4:SIC4Password@cluster0.vp0fgmb.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client['MyDatabase'] # ganti sesuai dengan nama database kalian
my_collections = db['Sensors'] # ganti sesuai dengan nama collections kalian

app = Flask(__name__)

# Route to handle the GET request
@app.route('/sensor1/temperature/avg', methods=['GET'])
def handle_get_request_temperature_avg():
    length = 0
    total_temperature = 0
    # Process the request and generate the response
    for my_collection in my_collections.find():
        print(my_collection.get('temperature'))
        total_temperature += my_collection.get('temperature')
        length += 1

    # Return the response as plain text
    return str(total_temperature/length)

# Route to handle the GET request
@app.route('/sensor1/kelembapan/avg', methods=['GET'])
def handle_get_request_humidity_avg():
    length = 0
    total_humidity = 0
    # Process the request and generate the response
    for my_collection in my_collections.find():
        print(my_collection.get('humidity'))
        total_humidity += my_collection.get('humidity')
        length += 1

    # Return the response as plain text
    return str(total_humidity/length)

if __name__ == '__main__':
    app.run()