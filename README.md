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
https://www.tutorialspoint.com/flask/flask_templates.htm
https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
https://towardsdatascience.com/serving-a-machine-learning-model-via-rest-api-5a4b38c02e90
https://www.statworx.com/ch/blog/how-to-build-a-machine-learning-api-with-python-and-flask/

https://www.kdnuggets.com/2019/01/build-api-machine-learning-model-using-flask.html


@prediction_app.route("/v1/inference/random_forest_model", methods=['POST'])
def inference():
    if request.method == 'POST':
        json_data = request.get_json()
        _logger.info(f'Inputs: {json_data}')

        result = predict(input_data=json_data)
        _logger.info(f'Outputs: {result}')

        predictions = result.get('predictions')[0]
        version = result.get('version')

        return jsonify({'predictions': predictions,
                        'version': version})