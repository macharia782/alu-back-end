# API - Employee Data Gathering & Export

## Description
This project demonstrates how to consume a REST API using Python (`requests`) to fetch employee records and TODO task progress from [JSONPlaceholder](https://jsonplaceholder.typicode.com/), process the structured JSON responses, and export the data into CSV and JSON formats.

## Requirements
* **OS:** Ubuntu 14.04 LTS / 20.04 LTS
* **Python:** Python 3.4.3+
* **Style:** PEP 8 compliant (`pycodestyle` / `pep8`)
* **Libraries:** `requests`, `csv`, `json`, `sys`

## Files & Tasks

| File | Description |
| :--- | :--- |
| `0-gather_data_from_an_API.py` | Fetches and prints an employee's completed TODO tasks and overall progress to `stdout` for a given employee ID. |
| `1-export_to_CSV.py` | Exports all TODO tasks owned by a given employee ID to `<USER_ID>.csv`. |
| `2-export_to_JSON.py` | Exports all TODO tasks owned by a given employee ID to `<USER_ID>.json`. |
| `3-dictionary_of_list_of_dictionaries.py` | Fetches and exports all TODO tasks across all employees into `todo_all_employees.json`. |
