#!/usr/bin/python3
"""Python script that that uses REST API, for a given employee ID,
   returns information about his/her TODO list progress
"""
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]
    name = requests.get("http://jsonplaceholder.typicode.com/users/{}"
                        .format(emp_id)).json().get("name")
    total_tasks = 0
    done_tasks = []
    req = requests.get("http://jsonplaceholder.typicode.com/todos").json()

    for task in req:
        if (task.get("userId") == int(emp_id)):
            total_tasks += 1
            if (task.get("completed")):
                done_tasks.append(task.get("title"))

    print("Employee {} is done with tasks({:d}/{:d}):"
          .format(name, len(done_tasks), total_tasks))

    for item in done_tasks:
        print("\t {}".format(item))
