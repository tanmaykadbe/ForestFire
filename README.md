🔥 Fire Weather Index (FWI) Prediction
This project is a machine learning web application that predicts the Fire Weather Index (FWI) based on meteorological and environmental input features. The goal is to help forecast fire risk using historical data and regression-based models.

🚀 Project Overview
🔍 Input Parameters:

Temperature (°C)

Relative Humidity (RH)

Wind Speed (Ws)

Rain (mm)

FFMC (Fine Fuel Moisture Code)

DMC (Duff Moisture Code)

ISI (Initial Spread Index)

Classes (Fire weather class)

Region (Geographic region)

📈 Models Used:

Lasso Regression

Ridge Regression

ElasticNet Regression

🌐 Web Interface:

Built using Flask.

Users can input weather and region parameters through a form and get a predicted FWI value.

🧠 Machine Learning Approach
The project includes the following steps:

Data Preprocessing

Handled missing values

Feature scaling and encoding

Train-test split

Model Training

Trained Lasso, Ridge, and ElasticNet regression models

Hyperparameter tuning using cross-validation

Evaluated performance using metrics like RMSE and R²

Deployment

Built a Flask web app for real-time prediction

Integrated the model into the backend for prediction
