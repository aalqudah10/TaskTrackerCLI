import argparse
import time
import json
import os

FILENAME = #Add the output JSON file

#Adding tasks to the file
def add_task(description):
    #Initiate the JSON file structure
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []  # If file is empty or invalid
    else:
        data = []
    
    #Count number of tasks already stored in the JSON file
    with open(FILENAME, 'r') as file:
        try:
            data = json.load(file)
            id = int(max(d['id'] for d in data)) + 1
        except:
            id = 1 #If empty then give and ID of '1'
    


    #Organize the task into a dictionary       
    task_info = {'id': id,
            'description': description,
            'status': 'todo',
            'createdAt' : time.ctime(time.time()),
            'updatedAt': time.ctime(time.time()) 
            }
    
    data.append(task_info)
    #Dump the updated list to the JSON file
    with open(FILENAME, 'w') as file:
        json.dump(data, file, indent=4)
    
    print(f'Task added successfully (ID: {task_info['id']})')
    pass


#Updating tasks 
def update_task(description, id):
    #Initiate the JSON file structure
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            try:
                data = json.load(file)
            except:
                pass # If file is empty or invalid
    else:
        pass

    #Searching for the target ID in the list of dictionaries
    for dictionary in data:
        #Updating description and time 
        if dictionary['id'] == id:
            dictionary['description'] = description
            dictionary['updatedAt'] = time.ctime(time.time())

    with open(FILENAME, 'w') as file:
        #Dump the updated data into the JSON file
        json.dump(data, file, indent=4)
    
    pass

#Changing task status
def taskStatus(target_status, target_id):
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                pass  # If file is empty or invalid
    else:
        pass
    
    #Searching for the target ID in the list of dictionaries
    for dictionary in data:
        if dictionary['id'] == target_id:
            #Updating the time
            dictionary['updatedAt'] = time.ctime(time.time())
            #Updating to the new status
            if target_status == 'in-progress':
                dictionary['status'] = 'in-progress'
            else:
                dictionary['status'] = 'done'

    with open(FILENAME, 'w') as file:
        #Dump the updated data into the JSON file
        json.dump(data, file, indent=4)
    
    pass

#Deleting task
def delete_task(target_id):
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                pass  # If file is empty or invalid
    else:
        pass   

    #Creating a new list of dictionaries with out the deleted task
    data = [d for d in data if d['id'] != target_id]
    
    #Dump the updated data into the JSON file
    with open(FILENAME, 'w') as file:
        json.dump(data, file, indent=4)
    pass

#Listing tasks 
def list_tasks(status):
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                pass # If file is empty or invalid
    else:
        pass

    #If wanting to list all tasks present in the JSON file
    tasks_to_be_listed = data

    #To list the data based on it's status (todo, in-progress, done)
    if status != None:
        tasks_to_be_listed = []
        for dictionary in data:
            if dictionary ['status'] == status:
                #Append the tasks to the new list based on its status
                tasks_to_be_listed.append(dictionary)
    
    for task in tasks_to_be_listed:
        #Printing the task along with its ID 
        print(f'ID = {task['id']} Task = {task['description']}')
    pass
    







def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    #Add Sub-Command
    add_parser = subparsers.add_parser('add', help = "Enter the task you want to add.")
    add_parser.add_argument('task', type = str)

    #Update Sub-Command
    update_parser = subparsers.add_parser('update', help = "Enter the ID of the task you want to update.")
    update_parser.add_argument('id', type = int)
    update_parser.add_argument('task', type = str)


    #Delete Sub-Command
    delete_parser = subparsers.add_parser('delete', help = "Enter the ID of the task you want to delete.")
    delete_parser.add_argument('id', type = int)

    #Mark-in-progress Sub-Command
    markprogress_parser = subparsers.add_parser("mark-in-progress", help = "Enter the ID of the task you want to mark in progress.")
    markprogress_parser.add_argument('id', type = int)

    #Mark-done Sub-Command
    markdone_parser = subparsers.add_parser("mark-done", help = "Enter the ID of the task you want to mark done.")
    markdone_parser.add_argument('id', type = int)

    #List Sub-Command
    list_parser = subparsers.add_parser('list', help='List tasks by status')
    list_parser.add_argument(
        'status',
        nargs='?', #Making the argument optional
        choices=['todo', 'in-progress', 'done'],
        help='Status to filter tasks by'
    )

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.task)

    elif args.command == 'update':
        update_task(args.task, args.id)

    elif args.command == 'delete':
        delete_task(args.id)

    elif args.command == 'mark-in-progress':
        taskStatus('in-progress', args.id)

    elif args.command == 'mark-done':
        taskStatus('done', args.id)

    elif args.command == 'list':
        list_tasks(args.status)
    

if __name__ == "__main__":
    main()
