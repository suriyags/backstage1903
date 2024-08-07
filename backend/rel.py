import json
from flask import Flask,request
from flask_cors import CORS
# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL
CORS(app) 
@app.route('/get_release', methods=['POST'])

def release():
    response = request.get_json()
    with open('data.json', 'w') as rd:
        json.dump(response, rd, indent=4)

    return "completed"


@app.route('/get_device', methods=['GET'])

def releaseinfo():
    with open('device.json', 'r') as rd:
        devinfo = json.load(rd)
    
    return devinfo


if __name__ == '__main__':
    print("processing")
    app.run(host='0.0.0.0',port='8091',debug=True)
