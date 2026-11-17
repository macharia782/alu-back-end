#!/usr/bin/python3
"""Exports all TODO tasks for a given employee ID to a CSV file."""
import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    emp_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user_res = requests.get("{}/users/{}".format(base_url, emp_id)).json()
    todos_res = requests.get(
        "{}/todos".format(base_url), params={"userId": emp_id}
    ).json()

    username = user_res.get("username")
    filename = "{}.csv".format(emp_id)

    with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_res:
            writer.writerow([
                emp_id,
                username,
                task.get("completed"),
                task.get("title")
                ])
