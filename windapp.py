# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np
# pandas for dataframes - though maynot use data frames
import pandas as pd
# may not use matplotlib either
import matplotlib as plt
from flask import jsonify
import tensorflow as tf


# jsonfy??

#flask is allowing remote interaction with python script


# Create a new web app. creating a new app in memory
app = fl.Flask(__name__)

#fl.Response()

# Add root route.
@app.route("/") # @app is a decorator
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