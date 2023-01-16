#!/usr/bin/python3
""" return employee information in JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user_id = sys.argv[1]
    user = '{}users/{}'.format(url, user_id)
    res = requests.get(user)
    json_o = res.json()
    name = json_o.get('username')

    todos = '{}todos?userId={}'.format(url, user_id)
    res = requests.get(todos)
    tasks = res.json()
    l_task = []
    for task in tasks:
        dict_task = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": name}
        l_task.append(dict_task)

    d_task = {str(user_id): l_task}
    filename = '{}.json'.format(user_id)
    with open(filename, mode='w') as f:
        json.dump(d_task, f)
