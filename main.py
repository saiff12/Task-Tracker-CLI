import sys
import json
import os
from datetime import datetime
TASKS_FILE = 'taskData.json'

def getDateTime():
     current_datetime = datetime.now()
     formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
     return formatted_datetime

def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(TASKS_FILE):
        return {}  
    with open(TASKS_FILE, 'r') as f:
        content = f.read().strip()
    if not content:
        return {}
    return json.loads(content)
    
def addTask(desc):
    taskData = load_tasks()
    currentDateTime = getDateTime()
    if  len(taskData.keys()):
        id = int(max(list(taskData.keys()))) + 1
    else:
        id = 1
    taskData[id] = dict()
    taskData[id]["desc"] = desc
    taskData[id]["status"] = "todo"
    taskData[id]["createdAt"] = currentDateTime
    taskData[id]["updatedAt"] = currentDateTime
    with open(TASKS_FILE, 'w') as json_file:
        json.dump(taskData, json_file)
    print("Task added successfully ID:", id)

def updateTask(id,desc):
    taskData = load_tasks()
    currentDateTime = getDateTime()
    try:
        taskData[id]["desc"] = desc
        taskData[id]["status"] = "todo"
        taskData[id]["updatedAt"] = currentDateTime
    except KeyError:
        print('Invalid task ID:', id)
        print("update failed")
        return
    with open(TASKS_FILE, 'w') as json_file:
        json.dump(taskData, json_file)
    print("Task id:",id,"updated successfully")
    

def deleteTask(id):
    taskData = load_tasks()
    try:
        del taskData[id]
    except KeyError:
        print('Invalid task ID:', id)
        print("delete failed")
        return
    with open(TASKS_FILE, 'w') as json_file:
        json.dump(taskData, json_file)
    print("Task id:",id,"deleted successfully")

def updateTaskStatus(id,status):
    taskData = load_tasks()
    currentDateTime = getDateTime()
    try:
        taskData[id]["status"] = status
        taskData[id]["updatedAt"] = currentDateTime
    except KeyError:
        print("invalid task ID:", id)
        print("update failed")
        return
    with open(TASKS_FILE, 'w') as json_file:
        json.dump(taskData, json_file)
    print("Task status updated successfully")

def listTasks(tasks, status=None):
    print("List of tasks:")
    if status is None:
        for key,value in tasks.items():
            print("Task ID:", key)
            print("Description:", value["desc"])
            print("Status:", value["status"])
            print("Created at:", value["createdAt"])
            print("Updated at:", value["updatedAt"])
            print()
    else:
        for key,value in tasks.items():
            if value["status"] == status:
                print("Task ID:", key)
                print("Description:", value["desc"])
                print("Status:", value["status"])
                print("Created at:", value["createdAt"])
                print("Updated at:", value["updatedAt"])
                print()


argsCount = len(sys.argv) 
if argsCount <= 1:
    print("enter a command through command line")
else:
    arg1 = sys.argv[1] 
    match arg1:
        case "add": 
            addTask(sys.argv[2])
        case "update":
            updateTask(sys.argv[2], sys.argv[3])
        case "delete":
            deleteTask(sys.argv[2])
        case "mark-in-progress":
            updateTaskStatus(sys.argv[2],"in-progress")
        case "mark-done":
            updateTaskStatus(sys.argv[2],"done")
        case "list":
            if argsCount == 2:
                print(listTasks(load_tasks()))
            elif argsCount == 3:
                print(listTasks(load_tasks(), sys.argv[2]))
        case _:
            print("invalid action")
                    