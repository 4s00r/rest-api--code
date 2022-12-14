# app for send json data

import requests
import json
URL= "http://127.0.0.1:8000/stucreate/"

data= {
  # it is a python dict data  
  'name':'sonam',
  'roll':100,
  'city': 'ranchi',
}

# convert dict to json data
json_data = json.dumps(data)
print (json_data)
# send request with post data and receive respoce data

r = requests.post(url = URL, data = json_data)
data = r.json()
print(data)