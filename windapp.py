# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np
import json
from flask import jsonify, request
import tensorflow as tf
from tensorflow.keras.models import load_model




# jsonfy??

#flask is allowing remote interaction with python script


# Create a new web app. creating a new app in memory
app = fl.Flask(__name__)
# load model
model = load_model('./wind.h5')
# possibly used for validation
EXPECTED = {
"speed":{"min":0.0,"max":25.0},
"power":{"min":0.0,"max":113.556}
}


# Add root route.
@app.route("/") # @app is a decorator
def home():
  return app.send_static_file('index.html')# sends a web page to home page

# Add prediction route.
@app.route('/predict', methods =['POST'])
def predict():
  data={"success":False}
  #get data from post request
  #data = request.get_json()
  reqData = request.form
  if(reqData == None):
    reqData = request.form
  if(reqData != None):
    readValue = float(reqData['value'])
    store_value = np.array([readValue])
    x = model.predict(store_value)
    list = x.tolist()
    json_string = json.dumps(list)
    data["response"] = json_string
    data["success"] = True
  return fl.jsonify(data)
  

  #return {"value": np.random.normal()}# key value pair

