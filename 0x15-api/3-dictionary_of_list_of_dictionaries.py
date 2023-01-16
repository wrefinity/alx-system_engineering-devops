#!/usr/bin/python3
""" a script to format information in dictionary format"""
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users'.format(url)
    res = requests.get(user)
    json_o = res.json()
    d_task = {}
    for user in json_o:
        name = user.get('username')
        user_id = user.get('id')
        todos = '{}todos?userId={}'.format(url, user_id)
        res = requests.get(todos)
        tasks = res.json()
        l_task = []
        for task in tasks:
            dictn = {"username": name,
                         "task": task.get('title'),
                         "completed": task.get('completed')}
            l_task.append(dictn)

        d_task[str(user_id)] = l_task
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as f:
        json.dump(d_task, f)
