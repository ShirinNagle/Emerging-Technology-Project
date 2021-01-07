# Emerging-Technology-Project
Repository for Emerging Technology Project

## Project Specifications

In this project you must create a web service that uses machine learning to make predictions
based on the data set powerproduction available on Moodle. The goal is to
produce a model that accurately predicts wind turbine power output from wind speed
values, as in the data set. You must then develop a web service that will respond with
predicted power values based on speed values sent as HTTP requests. 

To enhance your submission, you might consider developing and comparing more than
one model.

# Wind Power prediction app.

Included in this repository is a jupyter notebook, titled windPower.ipynb. This notebook was used to train a wind power output prediction model. 
A web API titled windapp.py. Also included two datasets, one with the original data and the other with all 0's removed. Some models were created from the data set with no 0's, this was in the interest of comparison. It was quite difficult to bring the loss down to a low number to improve accuracy with random occurrences of 0 throughout the dataset. The 0's accounted for almost 10% of the data set, which has a bearing on what the predicted output is. The model produced with the dataset with no 0's was not used in the Web API, the model that had the least amount of loss was used as the model for the Web API.


## Instructions to run Web Service

### Linux
```bash
export FLASK_APP=windapp.py
python3 -m flask run
```

### Windows
```bash
set FLASK_APP=windapp.py
python -m flask run
```
### Docker
```bash
docker build . -t windapp-image
docker run --name windapp-container -d -p 5000:5000 windapp-image
```


## How to run Jupyter Notebook[1].
1. Ensure Anaconda is installed on your computer.
2. Clone this repository to your computer.
3. Navigate to where you have cloned the repository, using cmd(Windows)
4. Type jupyter notebook on the cmd, this will launch a new browser window or new tab.
5. When started, the Jupyter Notebook App can access only files within its start-up folder (including any sub-folder). 
No configuration is necessary if you place your notebooks in your home folder or subfolders.
6. Double click on the file titled jupyter-tasks.ipynb
7. The notebook should open, with all tasks displayed and the work involved in proving these tasks.
8. For further information please see link below.

#### References
[1] Running the Jupyter Notebook; https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html
