#!/usr/bin/python3
"""Display the TODO list progress of an employee from a REST API."""
import json
import sys
import urllib.request


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    emp_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user_url = "{}/users/{}".format(base_url, emp_id)
    todos_url = "{}/todos?userId={}".format(base_url, emp_id)

    with urllib.request.urlopen(user_url) as response:
        user = json.loads(response.read().decode("utf-8"))

    with urllib.request.urlopen(todos_url) as response:
        todos = json.loads(response.read().decode("utf-8"))

    done = [t for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    for task in done:
        print("\t {}".format(task.get("title")))
