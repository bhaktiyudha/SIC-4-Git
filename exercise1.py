from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask, request, jsonify

uri = "mongodb+srv://SIC4:SIC4Password@cluster0.vp0fgmb.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client['MyDatabase'] # ganti sesuai dengan nama database kalian
my_collections = db['Sensors'] # ganti sesuai dengan nama collections kalian

app = Flask(__name__)

# Route to handle the POST request
@app.route('/sensor1', methods=['POST'])
def handle_post_request():
    # Get the parameters from the POST request
    data = request.get_json()

    # Check if the required parameters are present
    if 'temperature' in data and 'humidity' in data and 'time' in data:
        temperature = data['temperature']
        humidity = data['humidity']
        time = data['time']

        # Prepare your JSON data
        json_data = {'temperature': temperature, 'humidity': humidity, 'time': time}

        results = my_collections.insert_many([json_data])
        print(results)
        return jsonify({"message": "Success"})
    else:
        # If the required parameters are not present, return an error
        return jsonify({"error": "Invalid parameters"}), 400

if __name__ == '__main__':
    app.run()
