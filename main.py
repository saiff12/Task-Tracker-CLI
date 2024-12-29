import sys
import json
import os
from datetime import datetime
TASKS_FILE = 'taskData.json'

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
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    currentData = load_tasks()

    if  len(currentData.keys()):
        id = int(max(list(currentData.keys()))) + 1
    else:
        id = 1
    currentData[id] = dict()
    currentData[id]["desc"] = desc
    currentData[id]["status"] = "todo"
    currentData[id]["createdAt"] = formatted_datetime
    currentData[id]["updatedAt"] = formatted_datetime

    with open(TASKS_FILE, 'w') as json_file:
        json.dump(currentData, json_file)

    print("Task added successfully ID:", id)

def updateTask():
        pass
def deleteTask():
        pass
def updateTaskStatus(id,status):
        pass

arg1 = sys.argv[1] 
#arg3 = sys.argv[3]
argsCount = len(sys.argv) 
match arg1:
    case "add": 
        arg2 = sys.argv[2]  
        addTask(arg2)
    case "update":
        pass
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
                    
            
             
