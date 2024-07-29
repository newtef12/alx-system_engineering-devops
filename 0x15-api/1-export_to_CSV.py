#!/usr/bin/python3
"""Python script that that uses REST API, for a given employee ID,
   returns information about his/her TODO list progress
   but this time as a csv format
"""


import csv
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
            temp = []
            temp.extend((emp_id,
                         username,
                         task.get("completed"),
                         task.get("title")))
            all_tasks.append(temp)

    with open("{}.csv".format(emp_id), 'w+') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(all_tasks)
