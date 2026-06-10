import sys
import json
from datetime import datetime
import os

def add_expense(amount,category):
    with open("expense.json","r") as f:
        expenses=json.load(f)
    ID = len(expenses)+1
    expenses.append({"id": ID, "amount": amount, "category": category, "date": datetime.now().isoformat()})  
    with open("expense.json","w") as f:
        json.dump(expenses,f)
        print("Expense was successfully added")

def list_expense():
    with open("expense.json","r") as f:
        expenses=json.load(f)
    for expense in expenses:
        print(f"ID: {expense['id']}, Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense['date']}")

def delete_expense(expense_id):
    with open("expense.json","r") as f:
        expenses=json.load(f)
    for expense in expenses:
        if(expense["id"]==expense_id):
            expenses.remove(expense)
            with open("expense.json","w") as f:
                json.dump(expenses,f)
                print("Expense was successfully deleted")
            return
    print("Expense not found")

def update_expense(expense_id,amount,category):
    with open("expense.json","r") as f:
        expenses=json.load(f)
    for expense in expenses:
        if(expense["id"]==expense_id):
            expense["amount"]=amount
            expense["category"]=category
            with open("expense.json","w") as f:
                json.dump(expenses,f)
                print("Expense was successfully updated")
            return
    print("Expense not found")

def summary():
    with open("expense.json","r") as f:
        expenses=json.load(f)
    summary={}
    for expense in expenses:
        if expense["category"] in summary:
            summary[expense["category"]]+=expense["amount"]
        else:
            summary[expense["category"]]=expense["amount"]
    for category, total in summary.items():
        print(f"Category: {category}, Total: {total}")

def monthly_summary(month):
    with open("expense.json", "r") as f:
        expenses = json.load(f)
    total = 0
    for expense in expenses:
        expense_month = datetime.fromisoformat(
            expense["date"]
        ).month
        if expense_month == month:
            total += expense["amount"]
    print(f"Total expenses for month {month}: ${total}")

if(len(sys.argv)<2):
    print("Usage: python3 expense.py <command> [arguments]")
    sys.exit(1)
else:
    command= sys.argv[1]

if command=="add":
    if(len(sys.argv)<4):
        print("Usage: python3 expense.py add <amount> <category>")
        sys.exit(1)
    try:
        amount=float(sys.argv[2])
    except ValueError:
        print("Amount must be a number.")
        sys.exit(1)
    category=sys.argv[3]
    add_expense(amount,category)
elif command=="list":
    list_expense()
elif command=="delete":
    if(len(sys.argv)<3):
        print("Usage: python3 expense.py delete <expense_id>")
        sys.exit(1)
    try:
        expense_id=int(sys.argv[2])
    except ValueError:
        print("Expense ID must be an integer.")
        sys.exit(1)
    delete_expense(expense_id)
elif command=="update":
    if(len(sys.argv)<5):
        print("Usage: python3 expense.py update <expense_id> <amount> <category>")
        sys.exit(1)
    try:
        expense_id=int(sys.argv[2])
        amount=float(sys.argv[3])
    except ValueError:
        print("Expense ID must be an integer and Amount must be a number.")
        sys.exit(1)
    category=sys.argv[4]
    update_expense(expense_id,amount,category)
elif command=="summary":
    summary()
elif command=="monthly_summary" or command=="monthly":
    if(len(sys.argv)<3):
        print("Usage: python3 expense.py monthly_summary <month>")
        sys.exit(1)
    try:
        month=int(sys.argv[2])
        if month < 1 or month > 12:
            raise ValueError
    except ValueError:
        print("Month must be an integer between 1 and 12.")
        sys.exit(1)
    monthly_summary(month)
else:
    print("Unknown command. Available commands: add, list, delete, update, summary, monthly_summary")

