# Emerging-Technology-Project
Repository for Emerging Technology Project
## Instructions
In this project you must create a web service that uses machine learning to make predictions
based on the data set powerproduction available on Moodle. The goal is to
produce a model that accurately predicts wind turbine power output from wind speed
values, as in the data set. You must then develop a web service that will respond with
predicted power values based on speed values sent as HTTP requests. 

To enhance your submission, you might consider developing and comparing more than
one model.

# Wind Power prediction app.

# Linux
```bash
export FLASK_APP=windapp.py
python3 -m flask run
```

# Windows
```bash
set FLASK_APP=windapp.py
python -m flask run
```

```bash
docker build . -t windapp-image
docker run --name windapp-container -d -p 5000:5000 windapp-image
```

https://towardsdatascience.com/wind-energy-trade-with-deep-learning-time-series-forecasting-580bd41f163
https://machinelearningmastery.com/start-here/
https://www.kdnuggets.com/2018/05/complete-guide-convnet-tensorflow-flask-restful-python-api.html