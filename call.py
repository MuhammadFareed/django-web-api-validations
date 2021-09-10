import requests
import json

GET_URL = 'http://127.0.0.1:8000/get_students/'
POST_URL = 'http://127.0.0.1:8000/create_student/'
UPDATE_URL = 'http://127.0.0.1:8000/update_student/'
DELETE_URL = 'http://127.0.0.1:8000/delete_student/'

def get_student(id = None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    response = requests.get(url=GET_URL, data=json_data)
    json_response = response.json()
    print('response for get ========> ', json_response)

def create_student():
    data = {
        'name': 'Saqib',
        'roll': 11,
        'city': 'Isb'
    }
    json_data = json.dumps(data)
    response = requests.post(url=POST_URL, data=json_data)
    json_response = response.json()
    print('response for post ========> ', json_response)

def update_student(id):
    data = {
        'id': id,
        'name': 'Fareed8',
        'roll': 8,
    }
    json_data = json.dumps(data)
    response = requests.put(url=UPDATE_URL, data=json_data)
    json_response = response.json()
    print('response for update ========> ', json_response)

def delete_student(id):
    data = {'id': id}
    json_data = json.dumps(data)
    response = requests.delete(url=DELETE_URL, data=json_data)
    json_response = response.json()
    print('response for delete ========> ', json_response)



# Getting data for all students
get_student()

# Getting student data with id = 2
get_student()

# Creating new student
create_student()

# Updating student data with id 6
update_student(3)

# Deleteing student data with id 8
delete_student(3)