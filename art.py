
import requests
import json
from jinja2 import StrictUndefined
import random

base_url = 'https://collectionapi.metmuseum.org/public/collection/v1/'

def dept_call():
    
    res = requests.get(base_url + "departments")
    result = res.json()
    depts = result['departments']

    return depts

def find_dept(dept_name):

    depts = dept_call()

    for dept in depts:
        if dept['displayName'] == 'Egyptian Art':
            dept_id = dept['departmentId']

    return dept_id

def find_objs_in_dept(dept_id):

    dept_id = str(dept_id)

    res = requests.get(base_url + "objects?departmentIds=" + dept_id)
    result = res.json()
    obj_ids = result['objectIDs']

    return obj_ids

def ten_objs(obj_ids):

    artwork_display = []
    artwork_ids = random.choices(obj_ids, k=100)

    for id in artwork_ids:        
        res = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}")
        result = res.json()
        if len(result['primaryImage']) > 0 and len(artwork_display) < 10:
            artwork_display.append({'object_ID': result['objectID'], 'img_url': result['primaryImage'],
            'title': result['title'], 'artist_name': result['artistDisplayName'], 'obj_url': result['objectURL']})

    return artwork_display