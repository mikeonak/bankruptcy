#!/usr/bin/env python
# coding: utf-8



import pickle
from flask import Flask
from flask import request
from flask import jsonify
import xgboost as xgb
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler


with open('bankruptcy.bin','rb') as f_in:
    sc_X, model = pickle.load(f_in)
    print(sc_X)

app = Flask('bankruptcy')
@app.route('/predict', methods=['POST'])

def predict():
    firm = request.get_json()
    test_arr = np.array(firm)
    test_arr = test_arr.reshape(1,len(test_arr))
    X = sc_X.transform(test_arr)
    features = model.feature_names
    dtest = xgb.DMatrix(X,  feature_names=features)
    y_pred = model.predict(dtest)[0]
    success = y_pred > 0.16
    result={
        'default probability':str(y_pred),
        'Warning':bool(success)
    }

    return jsonify(result)





if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0.', port=9696)