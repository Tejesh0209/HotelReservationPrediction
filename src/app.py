import os
import joblib
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import MODEL_OUTPUT_PATH
from utils.common_functions import read_yaml_file

logger = get_logger(__name__)

app = Flask(__name__)

# Load the trained model
try:
    model = joblib.load(MODEL_OUTPUT_PATH)
    config = read_yaml_file('config/config.yaml')
    logger.info(f"Model loaded successfully from {MODEL_OUTPUT_PATH}")
except Exception as e:
    logger.error(f"Failed to load model: {str(e)}")
    model = None

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "model_loaded": model is not None}), 200

@app.route('/predict', methods=['POST'])
def predict():
    """
    Prediction endpoint
    Expected JSON input:
    {
        "data": [[feature1, feature2, ..., feature17]]
    }
    """
    try:
        if model is None:
            return jsonify({"error": "Model not loaded"}), 500
        
        request_json = request.get_json()
        
        if 'data' not in request_json:
            return jsonify({"error": "Missing 'data' field in request"}), 400
        
        # Convert input data to DataFrame
        features = request_json['data']
        
        if not isinstance(features, list) or len(features) == 0:
            return jsonify({"error": "Invalid data format"}), 400
        
        # Create DataFrame with proper column names
        categorical_columns = config.get('categorical_columns', [])
        numerical_columns = config.get('numerical_columns', [])
        all_columns = categorical_columns + numerical_columns
        
        df = pd.DataFrame(features, columns=all_columns)
        
        # Make prediction
        predictions = model.predict(df)
        probabilities = model.predict_proba(df) if hasattr(model, 'predict_proba') else None
        
        response = {
            "predictions": predictions.tolist(),
            "probabilities": probabilities.tolist() if probabilities is not None else None
        }
        
        logger.info(f"Prediction successful for {len(features)} sample(s)")
        return jsonify(response), 200
    
    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/predict-single', methods=['POST'])
def predict_single():
    """
    Single sample prediction endpoint
    Expected JSON input:
    {
        "features": {
            "feature1": value1,
            "feature2": value2,
            ...
        }
    }
    """
    try:
        if model is None:
            return jsonify({"error": "Model not loaded"}), 500
        
        request_json = request.get_json()
        
        if 'features' not in request_json:
            return jsonify({"error": "Missing 'features' field in request"}), 400
        
        features_dict = request_json['features']
        
        # Create DataFrame from dictionary
        df = pd.DataFrame([features_dict])
        
        # Make prediction
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0] if hasattr(model, 'predict_proba') else None
        
        response = {
            "prediction": int(prediction),
            "probability": probability.tolist() if probability is not None else None
        }
        
        logger.info(f"Single prediction successful: {prediction}")
        return jsonify(response), 200
    
    except Exception as e:
        logger.error(f"Error during single prediction: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
