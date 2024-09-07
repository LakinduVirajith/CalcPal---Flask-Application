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

# Load the Sequential diagnosis model
try:
    with open(os.path.join(models_directory, "sequential_diagnosis_model.pkl"), "rb") as f:
        sequential_model = pickle.load(f)
except Exception as e:
    raise RuntimeError(f"Failed to load the sequential diagnosis model: {str(e)}")

# Load the Visual diagnosis model
try:
    with open(os.path.join(models_directory, "visual_diagnosis_model.pkl"), "rb") as f:
        visual_model = pickle.load(f)
except Exception as e:
    raise RuntimeError(f"Failed to load the visual diagnosis model: {str(e)}")

# Load the Ideognostic diagnosis model
try:
    with open(os.path.join(models_directory, "ideognostic_diagnosis_model.pkl"), "rb") as f:
        ideognostic_model = pickle.load(f)
except Exception as e:
    raise RuntimeError(f"Failed to load the ideognostic_diagnosis_model diagnosis model: {str(e)}")

# Load the Operational diagnosis model
try:
    with open(os.path.join(models_directory, "operational_diagnosis_model.pkl"), "rb") as f:
        operational_model = pickle.load(f)
except Exception as e:
    raise RuntimeError(f"Failed to load the operational diagnosis model: {str(e)}")

# Load the Graphical diagnosis model
try:
    with open(os.path.join(models_directory, "graphical_diagnosis_mode.pkl"), "rb") as f:
        graphical_model = pickle.load(f)
except Exception as e:
    raise RuntimeError(f"Failed to load the graphical diagnosis model: {str(e)}")

# Load the Practognostic diagnosis model
try:
    with open(os.path.join(models_directory, "practognostic_diagnosis_model.pkl"), "rb") as f:
        practognostic_model = pickle.load(f)
except Exception as e:
    raise RuntimeError(f"Failed to load the practognostic diagnosis model: {str(e)}")

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
    
# Define the route for Sequential model prediction
@app.route('/sequential', methods=['POST'])
def sequential_predict():
    """
    Endpoint for making predictions using the Sequential diagnosis model.
    Expects JSON input with features required by the model.
    """
    try:
        # Get JSON data from the request
        sequential_data = request.json
        print("Received data:", sequential_data)  # Debugging: Log received data

        # Convert the received data into a DataFrame for model prediction
        input_data = pd.DataFrame([sequential_data])

        # Make a prediction using the loaded lexical model
        prediction = sequential_model.predict(input_data)
        print("Prediction:", prediction)  # Debugging: Log prediction result

        # Interpret the prediction result (0 for False, 1 for True)
        result = bool(prediction[0])
        message = "Doesn't Have Sequential Dyscalculia" if not result else "Has Sequential Dyscalculia"
        
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
    
# Define the route for Visual model prediction
@app.route('/visual', methods=['POST'])
def visual_predict():
    """
    Endpoint for making predictions using the Visual diagnosis model.
    Expects JSON input with features required by the model.
    """
    try:
        # Get JSON data from the request
        visual_data = request.json
        print("Received data:", visual_data)  # Debugging: Log received data

        # Convert the received data into a DataFrame for model prediction
        input_data = pd.DataFrame([visual_data])

        # Make a prediction using the loaded lexical model
        prediction = visual_model.predict(input_data)
        print("Prediction:", prediction)  # Debugging: Log prediction result

        # Interpret the prediction result (0 for False, 1 for True)
        result = bool(prediction[0])
        message = "Doesn't Have Visual Dyscalculia" if not result else "Has Visual Dyscalculia"
        
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
    
# Define the route for Ideognostic model prediction
@app.route('/ideognostic', methods=['POST'])
def ideognostic_predict():
    """
    Endpoint for making predictions using the Ideognostic diagnosis model.
    Expects JSON input with features required by the model.
    """
    try:
        # Get JSON data from the request
        ideognostic_data = request.json
        print("Received data:", ideognostic_data)  # Debugging: Log received data

        # Convert the received data into a DataFrame for model prediction
        input_data = pd.DataFrame([ideognostic_data])

        # Make a prediction using the loaded lexical model
        prediction = ideognostic_model.predict(input_data)
        print("Prediction:", prediction)  # Debugging: Log prediction result

        # Interpret the prediction result (0 for False, 1 for True)
        result = bool(prediction[0])
        message = "Doesn't Have Ideognostic Dyscalculia" if not result else "Has Ideognostic Dyscalculia"
        
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
    
# Define the route for Operational model prediction
@app.route('/operational', methods=['POST'])
def operational_predict():
    """
    Endpoint for making predictions using the Operational diagnosis model.
    Expects JSON input with features required by the model.
    """
    try:
        # Get JSON data from the request
        operational_data = request.json
        print("Received data:", operational_data)  # Debugging: Log received data

        # Convert the received data into a DataFrame for model prediction
        input_data = pd.DataFrame([operational_data])

        # Make a prediction using the loaded lexical model
        prediction = operational_model.predict(input_data)
        print("Prediction:", prediction)  # Debugging: Log prediction result

        # Interpret the prediction result (0 for False, 1 for True)
        result = bool(prediction[0])
        message = "Doesn't Have Operational Dyscalculia" if not result else "Has Operational Dyscalculia"
        
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
    
# Define the route for Graphical model prediction
@app.route('/graphical', methods=['POST'])
def graphical_predict():
    """
    Endpoint for making predictions using the Graphical diagnosis model.
    Expects JSON input with features required by the model.
    """
    try:
        # Get JSON data from the request
        graphical_data = request.json
        print("Received data:", graphical_data)  # Debugging: Log received data

        # Convert the received data into a DataFrame for model prediction
        input_data = pd.DataFrame([graphical_data])

        # Make a prediction using the loaded lexical model
        prediction = graphical_model.predict(input_data)
        print("Prediction:", prediction)  # Debugging: Log prediction result

        # Interpret the prediction result (0 for False, 1 for True)
        result = bool(prediction[0])
        message = "Doesn't Have Graphical Dyscalculia" if not result else "Has Graphical Dyscalculia"
        
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
    
# Define the route for Practognostic model prediction
@app.route('/practognostic', methods=['POST'])
def practognostic_predict():
    """
    Endpoint for making predictions using the Practognostic diagnosis model.
    Expects JSON input with features required by the model.
    """
    try:
        # Get JSON data from the request
        practognostic_data = request.json
        print("Received data:", practognostic_data)  # Debugging: Log received data

        # Convert the received data into a DataFrame for model prediction
        input_data = pd.DataFrame([practognostic_data])

        # Make a prediction using the loaded lexical model
        prediction = practognostic_model.predict(input_data)
        print("Prediction:", prediction)  # Debugging: Log prediction result

        # Interpret the prediction result (0 for False, 1 for True)
        result = bool(prediction[0])
        message = "Doesn't Have Practognostic Dyscalculia" if not result else "Has Practognostic Dyscalculia"
        
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
