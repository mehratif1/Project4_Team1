from flask import Flask, render_template, request
import numpy as np
import lightgbm as lgb
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load your trained LightGBM model
model = joblib.load('model.pkl')
# model = lgb.Booster(model_file='model.pkl')

# Define a function to process the input and make prediction
def predict_difficulties(features):
    # Make prediction
    prediction = model.predict(features)
    return prediction

@app.route('/')
def index():
    return render_template('index.html')

# Define route for form submission
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input features from the form
    features = []
    for i in range(11):
        feature = float(request.form[f'feature{i+1}'])
        features.append(feature)
    
    # Make prediction
    prediction = predict_difficulties(np.array(features).reshape(1, -1))
    
    # Determine result
    result = "Will have difficulties" if prediction[0] == 1 else "Won't have difficulties"
    
    # Render the result template with the prediction result
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
