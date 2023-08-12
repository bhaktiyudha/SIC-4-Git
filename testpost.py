from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to handle the POST request
@app.route('/example', methods=['POST'])
def handle_post_request():
    # Get the parameters from the POST request
    data = request.get_json()

    # Check if the required parameters are present
    if 'name' in data and 'age' in data:
        name = data['name']
        age = data['age']

        # Process the parameters (you can perform any business logic here)
        result = f"Hello, {name}! You are {age} years old."

        # Return the response as JSON
        return jsonify({"message": result})
    else:
        # If the required parameters are not present, return an error
        return jsonify({"error": "Invalid parameters"}), 400

if __name__ == '__main__':
    app.run()
