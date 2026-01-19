import csv
import os

FILE = 'tasks.csv'

# Create file if it doesn't exist
if not os.path.exists(FILE):
    with open(FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Task", "Status"])

def show_tasks():
    with open(FILE, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def add_task(task):
    with open(FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([task, "Pending"])
    print(f"Task '{task}' added!")

def mark_done(task_name):
    tasks = []
    with open(FILE, 'r') as f:
        reader = csv.reader(f)
        tasks = list(reader)
    
    for row in tasks:
        if row[0] == task_name:
            row[1] = "Done"
    
    with open(FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(tasks)
    print(f"Task '{task_name}' marked as done!")

# CLI Menu
while True:
    print("\n1. Show tasks\n2. Add task\n3. Mark task done\n4. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        show_tasks()
    elif choice == "2":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "3":
        task = input("Enter task to mark done: ")
        mark_done(task)
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
