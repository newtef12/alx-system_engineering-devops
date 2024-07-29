#!/usr/bin/python3
"""Python script that that uses REST API, for a given employee ID,
   returns information about his/her TODO list progress
   this time exports data in the JSON format
"""

import json
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]
    username = requests.get("http://jsonplaceholder.typicode.com/users/{}"
                            .format(emp_id)).json().get("username")
    all_tasks = []
    req = requests.get("http://jsonplaceholder.typicode.com/todos").json()

    for task in req:
        if (task.get("userId") == int(emp_id)):
            temp = {}
            temp["task"] = task.get("title")
            temp["completed"] = task.get("completed")
            temp["username"] = username
            all_tasks.append(temp)

    with open("{}.json".format(emp_id), 'w+') as jsonfile:
        json.dump({emp_id: all_tasks}, jsonfile)
