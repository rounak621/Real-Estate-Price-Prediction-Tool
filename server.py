from flask import Flask, request, jsonify, render_template, send_from_directory
import util

# Initialize the Flask app
app = Flask(__name__, static_folder='../client', template_folder='../client')

@app.route('/')
def home():
    # Serve the main HTML page
    return render_template('app.html')

@app.route('/<path:filename>')
def serve_static_files(filename):
    # Serve static files (CSS, JS, etc.)
    return send_from_directory(app.static_folder, filename)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    # Fetch locations from util
    locations = util.get_location_names()
    response = jsonify({
        'Locations': locations
    })
    response.headers.add('Access-Control-Allow-Origin', '*')  # To allow cross-origin requests
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        # Get JSON data from the request body
        data = request.get_json()
        total_sqft = float(data['total_sqft'])
        location = data['location']
        bhk = int(data['bhk'])
        bath = int(data['bath'])

        # Get estimated price from util
        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
        response = jsonify({
            'estimated_price': estimated_price
        })
    except Exception as e:
        # Handle any errors and return as JSON
        response = jsonify({
            'error': str(e)
        })

    return response

if __name__ == '__main__':
    # Load model artifacts on server startup
    util.load_saved_artifacts()
    print("Flask server is running...")
    app.run(debug=True)
