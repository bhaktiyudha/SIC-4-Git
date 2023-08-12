from flask import Flask

app = Flask(__name__)

# Route to handle the GET request
@app.route('/example', methods=['GET'])
def handle_get_request():
    # Process the request and generate the response
    response = "This is a GET request response!"

    # Return the response as plain text
    return response

if __name__ == '__main__':
    app.run()