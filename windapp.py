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

model = load_model("./wind.h5")

# possibly use for validation in a more detailed version of the web server
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
  data = {"success":False}
  print(model)
  params = fl.request.form
  if(params == None):
    params = fl.request.form
  if(params != None):
    getValue = float(params['value'])
    arrayVal = np.array([getValue])
    x = model.predict(arrayVal)
    list = x.tolist()
    listStr = json.dumps(list)
    data["response"] = listStr
    data["success"] = True
  return fl.jsonify(data)
  

  

