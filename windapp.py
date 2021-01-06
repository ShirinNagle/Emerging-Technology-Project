# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np
# pandas for dataframes - though maynot use data frames
import pandas as pd
# may not use matplotlib either
import matplotlib as plt
from flask import jsonify, request
import tensorflow as tf
from tensorflow.keras.models import load_model

from markupsafe import escape #remove after testing


# jsonfy??

#flask is allowing remote interaction with python script


# Create a new web app. creating a new app in memory
app = fl.Flask(__name__)
# load model
model = load_model('wind_model.h5')
# possibly used for validation
EXPECTED = {
"speed":{"min":0.0,"max":25.0},
"power":{"min":0.0,"max":113.556}
}


# Add root route.
@app.route("/", methods=["POST"]) # @app is a decorator
def home():
 
  return app.send_static_file('index.html')# sends a web page to home page

# Add uniform route.
@app.route('/api/uniform') # api returns json
def uniform():
  return {"value": np.random.uniform()}# return a dictionary

# Add normal route.
@app.route('/api/normal')
def normal():
  return {"value": np.random.normal()}# key value pair


# Add prediction route.
@app.route('/api/predict', methods =['POST'])
def predict():
  #get data from post request
  data = request.get_json()
  df = pd.DataFrame(str(data['text']), columns=['power'])
  print (df.head())
  pred = model.predict(data_df=df)
  print(pred)
  return jsonify(pred['wind_model'], [0])

  #return {"value": np.random.normal()}# key value pair

