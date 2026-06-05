import json
import sys
import os
from datetime import datetime

def load_tasks():
    if not os.path.exists("tasks.json"): #if json file is empty
        return []

    with open("tasks.json", "r") as file:
        try:
            return json.load(file)  #extracting the data from json file and converting it to python format
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    with open("tasks.json", "w") as file: #open the json file in write mode and convert the python format to json format and save it in the file
        json.dump(tasks, file, indent=4)


# Check if command is provided
if len(sys.argv) < 2:
    print("Please provide a command.")
    sys.exit()

command = sys.argv[1]

# Add Task
if command == "add":

    if len(sys.argv) < 3:
        print("Please provide a task description.")
        sys.exit()

    description = sys.argv[2]
    tasks = load_tasks()
    new_id = len(tasks) + 1
    current_time = datetime.now().isoformat()

    task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": current_time,
        "updatedAt": current_time
    }

    tasks.append(task)

    save_tasks(tasks)

    print(f"Task added successfully (ID: {new_id})")

elif command == "list":
    tasks=load_tasks()
    if not tasks:
        print("no taks found")
    else:
        if len(sys.argv)==3:
            status=sys.argv[2]
            for task in tasks:
                if task['status']==status:
                    print(f"{task['id']} | {task['description']} | {task['status']} | {task['createdAt']} | {task['updatedAt']}")
        else:
            for task in tasks:
                print(f"{task['id']} | {task['description']} | {task['status']} | {task['createdAt']} | {task['updatedAt']}")

elif command== "update":
    if(len(sys.argv)<4):
        print("Please provide task ID and new description.")
        sys.exit()
    task_id=int(sys.argv[2])
    new_desc=sys.argv[3]

    tasks=load_tasks()

    f=False

    for task in tasks:
        if(task['id']==task_id):
            task['description']=new_desc
            task['updatedAt']=datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully.")
            f=True
            break
    if not f:
        print(f"Task with ID {task_id} not found.")
    
elif command == "delete":

    if len(sys.argv) < 3:
        print("Please provide task ID.")
        sys.exit()

    task_id = int(sys.argv[2])

    tasks = load_tasks()

    found = False

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"Task {task_id} deleted successfully.")
            found = True
            break

    if not found:
        print(f"Task with ID {task_id} not found.")

elif command == "mark-in-progress":

    if len(sys.argv) < 3:
        print("Please provide task ID.")
        sys.exit()

    task_id = int(sys.argv[2])

    tasks = load_tasks()

    found = False

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as in progress.")
            found = True
            break

    if not found:
        print(f"Task with ID {task_id} not found.")

elif command == "mark-done":

    if len(sys.argv) < 3:
        print("Please provide task ID.")
        sys.exit()

    task_id = int(sys.argv[2])

    tasks = load_tasks()

    found = False

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task["updatedAt"] = datetime.now().isoformat()

            save_tasks(tasks)

            print(f"Task {task_id} marked as done.")
            found = True
            break

    if not found:
        print(f"Task with ID {task_id} not found.")

else:
    print("Invalid command.")