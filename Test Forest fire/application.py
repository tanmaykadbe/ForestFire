from flask import Flask, request, jsonify, render_template
from sklearn.preprocessing import StandardScaler
import pickle 
import numpy as np
import pandas as pd

application = Flask(__name__)
app = application

ridge_model = pickle.load(open("models/ridge.pkl", "rb"))
StandardScaler = pickle.load(open("models/scaler.pkl", "rb"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predictdata", methods=["GET","POST"])
def predict_datapoint():
    if request.method == "POST":
        pass
    else:
        return render_template("home.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug= True, port=5000)
