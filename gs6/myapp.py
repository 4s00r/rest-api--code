# app for send json data
import requests
import json
URL= "http://127.0.0.1:8000/studentapi/"


def get_data(id = None):
  data={}
  if id is not None:
    data = {'id':id}
  json_data= json.dumps(data)
  r = requests.get(url = URL, data = json_data)
  data = r.json()
  print(r.status_code)
  print(data)


# get_data()

def post_data():
  data = {
    'name':'sonal',
    'roll':106,
    'city':'hazaribagh'
  }

  json_data = json.dumps(data)
  r = requests.post(url = URL, data = json_data)
  print(r.status_code)
  print(r.json())
  


# post_data()  

def update_data():
  data = {
    'id':6,
    'name':'jack',
    'city':'ranchi'
  }

  json_data = json.dumps(data)
  r = requests.put(url = URL, data = json_data)
  print(r.status_code)
  print(r.json())


# update_data()  

def delete_data():
  data = {'id':6 }

  json_data = json.dumps(data)
  r = requests.delete(url = URL, data = json_data)
  data = r.json()
  print(data)


delete_data()

