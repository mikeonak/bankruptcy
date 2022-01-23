#!/usr/bin/env python
# coding: utf-8

import json
import requests


url = "http://localhost:9696/predict"
firm = [-0.03939289,  0.07500932, -0.11583775, -0.00939272, -0.00122538,
        -0.01256204, -0.14048721, -0.42142507, -0.0689293 , -0.02312328,
        -0.01418585, -0.02576842, -0.08541529, -0.13184356]
j_data = json.dumps(firm)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
print(requests.post(url, data=j_data,headers=headers).json())


