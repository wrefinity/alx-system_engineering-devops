#!/usr/bin/python3
""" return employee information in csv format """

import csv
import json
import requests
import sys


def get_user_todo():
    emp_id = int(sys.argv[1])
    url1 = 'https://jsonplaceholder.typicode.com/users/%s' % emp_id
    url2 = '%s/todos' % url1
    todo_list = requests.get(url2).json()
    user = requests.get(url1).json()
    pat = "{}.csv".format(emp_id)

    with open(pat, 'w', encoding='utf-8') as fl:
        writer = csv.writer(fl, delimiter=',', quoting=csv.QUOTE_ALL)
        for todo in todo_list:
            writer.writerow([emp_id, user.get('username'),
                            todo.get('completed'), todo.get('title')])


if __name__ == '__main__':
    get_user_todo()
