from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import pandas as pd
import pickle

# Set up path to the models directory
models_directory = os.path.join(os.path.dirname(__file__), 'models')

# Load the Verbal diagnosis model
try:
    with open(os.path.join(models_directory, "verbal_diagnosis_model.pkl"), "rb") as f:
        verbal_model = pickle.load(f)
except Exception as e:
    raise RuntimeError(f"Failed to load the verbal diagnosis model: {str(e)}")

# Load the Lexical diagnosis model
try:
    with open(os.path.join(models_directory, "lexical_diagnosis_model.pkl"), "rb") as f:
        lexical_model = pickle.load(f)
except Exception as e:
    raise RuntimeError(f"Failed to load the lexical diagnosis model: {str(e)}")

# Initialize Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Define the home route
@app.route('/')
def home():
    """
    Simple home route to check if the server is running.
    """
    return "Welcome to the Dyscalculia Prediction Flask App!"

# Define the route for Verbal model prediction
@app.route('/verbal', methods=['POST'])
def verbal_predict():
    """
    Endpoint for making predictions using the Verbal diagnosis model.
    Expects JSON input with features required by the model.
    """
    try:
        # Get JSON data from the request
        verbal_data = request.json
        print("Received data:", verbal_data)  # Debugging: Log received data

        # Convert the received data into a DataFrame for model prediction
        input_data = pd.DataFrame([verbal_data])

        # Make a prediction using the loaded verbal model
        prediction = verbal_model.predict(input_data)
        print("Prediction:", prediction)  # Debugging: Log prediction result

        # Interpret the prediction result (0 for False, 1 for True)
        result = bool(prediction[0])
        message = "Doesn't Have Verbal Dyscalculia" if not result else "Has Verbal Dyscalculia"
        
        # Return the result as a JSON response
        return jsonify({'prediction': result, 'message': message})
    except KeyError as e:
        # Handle missing keys in the input JSON
        print("Missing key in input:", e)  # Debugging: Log error message
        return jsonify({'error': f"Missing key in input data: {str(e)}"}), 400
    except Exception as e:
        # Handle other exceptions
        print("Error occurred:", e)  # Debugging: Log error message
        return jsonify({'error': str(e)}), 500

# Define the route for Lexical model prediction
@app.route('/lexical', methods=['POST'])
def lexical_predict():
    """
    Endpoint for making predictions using the Lexical diagnosis model.
    Expects JSON input with features required by the model.
    """
    try:
        # Get JSON data from the request
        lexical_data = request.json
        print("Received data:", lexical_data)  # Debugging: Log received data

        # Convert the received data into a DataFrame for model prediction
        input_data = pd.DataFrame([lexical_data])

        # Make a prediction using the loaded lexical model
        prediction = lexical_model.predict(input_data)
        print("Prediction:", prediction)  # Debugging: Log prediction result

        # Interpret the prediction result (0 for False, 1 for True)
        result = bool(prediction[0])
        message = "Doesn't Have Lexical Dyscalculia" if not result else "Has Lexical Dyscalculia"
        
        # Return the result as a JSON response
        return jsonify({'prediction': result, 'message': message})
    except KeyError as e:
        # Handle missing keys in the input JSON
        print("Missing key in input:", e)  # Debugging: Log error message
        return jsonify({'error': f"Missing key in input data: {str(e)}"}), 400
    except Exception as e:
        # Handle other exceptions
        print("Error occurred:", e)  # Debugging: Log error message
        return jsonify({'error': str(e)}), 500

# Lists all available routes in the Flask application
@app.route('/routes')
def list_routes():
    """
    Endpoint to list all available routes in the Flask application.
    Provides route details including endpoint, methods, and URL.
    """
    routes = [
        {
            'endpoint': rule.endpoint,
            'methods': list(rule.methods - {'HEAD', 'OPTIONS'}),
            'url': rule.rule
        }
        for rule in app.url_map.iter_rules()
        if rule.endpoint != 'static'  # Exclude static files
    ]
    
    # Sort routes by URL for better readability
    routes.sort(key=lambda x: x['url'])
    
    # Create a formatted JSON response
    response = {
        'status': 'success',
        'message': 'List of available routes',
        'routes': routes
    }
    
    return jsonify(response)

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
