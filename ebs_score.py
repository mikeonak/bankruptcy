#!/usr/bin/env python
# coding: utf-8


import requests
import json


url = 'http://final-project-env.eba-j2gszuqm.eu-central-1.elasticbeanstalk.com/predict' 

firm = [-1.8312e-01,  5.1623e-01,  3.6906e-01,  2.7118e+00, -1.8077e-01,
       -1.9486e-01, -1.8077e-01,  3.2661e+00,  1.0798e+00,  2.4991e+02,
       -4.6749e-01, -2.9474e-01,  2.3021e-02,  4.7887e+00]
j_data = json.dumps(firm)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}


print(requests.post(url, data=j_data,headers=headers).json())


