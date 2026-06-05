# Task Tracker CLI

A simple Command Line Interface (CLI) application built with Python to manage and track tasks. Tasks are stored in a JSON file and can be added, updated, deleted, marked as in progress or done, and filtered by status.

## Features

* Add a new task
* Update an existing task
* Delete a task
* Mark a task as in progress
* Mark a task as done
* List all tasks
* List tasks by status (todo, in-progress, done)
* Store tasks in a JSON file
* Automatic task ID generation
* Track creation and update timestamps

## Requirements

* Python 3.x

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd task-tracker
```

2. Run the application using Python:

```bash
python3 task.py
```

## Usage

### Add a Task

```bash
python3 task.py add "Buy groceries"
```

### List All Tasks

```bash
python3 task.py list
```

### Update a Task

```bash
python3 task.py update 1 "Buy groceries and cook dinner"
```

### Delete a Task

```bash
python3 task.py delete 1
```

### Mark Task as In Progress

```bash
python3 task.py mark-in-progress 1
```

### Mark Task as Done

```bash
python3 task.py mark-done 1
```

### List Tasks by Status

```bash
python3 task.py list todo

python3 task.py list in-progress

python3 task.py list done
```

## Task Structure

Each task is stored in the following format:

```json
{
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2026-06-05T12:00:00",
    "updatedAt": "2026-06-05T12:00:00"
}
```

## Technologies Used

* Python
* JSON
* File Handling
* Command Line Arguments (`sys.argv`)
* Datetime Module

## Project Structure

```text
task-tracker/
│
├── task.py
├── tasks.json
└── README.md
```

## Author

Sneha Agrawal
