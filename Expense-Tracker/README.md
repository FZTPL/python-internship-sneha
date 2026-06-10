# Expense Tracker CLI

## Overview

Expense Tracker CLI is a command-line application built with Python that helps users manage their expenses. The application allows users to add, update, delete, and view expenses, as well as generate summaries of their spending.

Expense data is stored locally in a JSON file, making it simple, lightweight, and easy to use.

---

## Features

* Add new expenses
* View all expenses
* Update existing expenses
* Delete expenses
* View total expense summary
* View monthly expense summary
* Store data persistently using JSON
* Input validation and error handling

---

## Project Structure

```text
expense-tracker/
│
├── expense.py
├── expense.json
└── README.md
```

---

## Requirements

* Python 3.x

No external libraries are required.

---

## How to Run

Open a terminal and navigate to the project directory.

### Add an Expense

```bash
python expense.py add 20 Food
```

Output:

```text
Expense was successfully added
```

---

### List All Expenses

```bash
python expense.py list
```

Example Output:

```text
ID: 1, Amount: 20.0, Category: Food, Date: 2026-06-10T12:00:00
ID: 2, Amount: 15.0, Category: Coffee, Date: 2026-06-10T12:05:00
```

---

### Update an Expense

```bash
python expense.py update 1 30 Food
```

Output:

```text
Expense was successfully updated
```

---

### Delete an Expense

```bash
python expense.py delete 1
```

Output:

```text
Expense was successfully deleted
```

---

### View Total Expense Summary

```bash
python expense.py summary
```

Example Output:

```text
Total expenses: $45
```

---

### View Monthly Expense Summary

```bash
python expense.py monthly 6
```

Example Output:

```text
Total expenses for month 6: $45
```

---

## Data Storage

All expense records are stored in `expense.json`.

Example:

```json
[
  {
    "id": 1,
    "amount": 20.0,
    "category": "Food",
    "date": "2026-06-10T12:00:00"
  },
  {
    "id": 2,
    "amount": 15.0,
    "category": "Coffee",
    "date": "2026-06-10T12:05:00"
  }
]
```

---

## Error Handling

The application handles common errors such as:

* Invalid command usage
* Non-numeric amounts
* Invalid expense IDs
* Invalid month values
* Missing expenses
* Missing data file

---

## Future Improvements

* Add expense descriptions
* Add expense categories filtering
* Set monthly budgets
* Export expenses to CSV
* Improve CLI formatting with tables
* Use argparse for advanced command handling

---

## Technologies Used

* Python
* JSON
* File Handling
* Datetime Module
* Command Line Interface (CLI)

---

## Learning Outcomes

This project helped practice:

* Python fundamentals
* File handling
* JSON data management
* CRUD operations
* Command-line argument processing
* Input validation
* Error handling
* Working with dates and times
