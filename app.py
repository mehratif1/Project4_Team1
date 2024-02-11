# Import the dependencies.
import pandas as pd
from flask import Flask, jsonify , render_template
from flask import Flask, render_template, request, jsonify
import h5py
import numpy as np
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('credit_risk_model.pkl', 'rb'))


#################################################
# Flask Routes
#################################################
@app.route("/")
def homepage():
    """List of all the files."""
    return render_template ("index.html")
       
     

# Route for handling form submission and prediction
@app.route('/predict', methods=['POST'])
def predict():
    val1 = float(request.form['AMT_GOODS_PRICE'])
    val2 = float(request.form['DAYS_REGISTRATION'])
    val3 = float(request.form['DAYS_LAST_PHONE_CHANGE'])
    val4 = float(request.form['DAYS_EMPLOYED'])
    val5 = float(request.form['AMT_CREDIT'])
    # Convert input values to float and create array
    arr = np.array([val1, val2, val3, val4, val5])
    # Make prediction using the loaded model
    pred = model.predict(arr.reshape(1, -1))




@app.route("/credit_risk_data")
def credit_risk_data ():
    df= pd.read_csv('Resources/credit_risk_reduced.csv')
    df1=df.to_json(orient='records')
    df1=pd.read_json(df1)
    return jsonify(df1.to_dict(orient='records'))









if __name__=="__main__":
    app.run(debug=True)
