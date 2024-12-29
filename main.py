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
    taskKeys = taskData.keys()
    if  len(taskKeys):
        if id in taskKeys:
            taskData[id]["desc"] = desc
            taskData[id]["updatedAt"] = currentDateTime
            with open(TASKS_FILE, 'w') as json_file:
                json.dump(taskData, json_file)
            print("Task id:",id,"updated successfully")
        else:
            print("Invalid task ID")
    else:
        print("No tasks to update, add a task first!")

def deleteTask():
        pass
def updateTaskStatus(id,status):
        pass


argsCount = len(sys.argv) 
if argsCount == 1:
    print("enter a command through command line")
else:
    arg1 = sys.argv[1] 
    match arg1:
        case "add": 
            addTask(sys.argv[2])
        case "update":
            updateTask(sys.argv[2], sys.argv[3])
        case "delete":
            pass
        case "mark-in-progress":
            pass
        case "mark-done":
            pass
        case "list":
            if argsCount == 2:
                print(load_tasks())
            elif argsCount == 3:
                tasks = load_tasks()
                for key, value in tasks.items():
                    if (sys.argv[2] == value["status"]):
                        print(key, value)
                    
            
             
