import pickle
from flask import Flask,request,app,jsonify,url_for,rendor_template
import numpy as np
import pandas as pd

app=Flask(__name__)
## Load the Model
regmodel=pickle.load(open('regmodel.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)