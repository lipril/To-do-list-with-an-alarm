import time
from datetime import datetime, timedelta
import threading

# A class to manage the To-Do list
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, due_time=None):
        self.tasks.append({"task": task, "due_time": due_time})
        print(f"Task added: '{task}'{' with a reminder at ' + due_time if due_time else ''}")

    def show_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty!")
            return
        print("\nYour To-Do List:")
        for i, task in enumerate(self.tasks, 1):
            due_time = task['due_time']
            due_str = f" (Reminder set for: {due_time})" if due_time else ""
            print(f"{i}. {task['task']}{due_str}")
        print("")

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task removed: '{removed_task['task']}'")
        else:
            print("Invalid task number!")

# Function to set a reminder alarm
def set_reminder(task, due_time_str):
    due_time = datetime.strptime(due_time_str, "%Y-%m-%d %H:%M:%S")
    time_diff = (due_time - datetime.now()).total_seconds()
    if time_diff > 0:
        threading.Timer(time_diff, alarm, args=[task]).start()
    else:
        print("Reminder time is in the past. Please set a future time.")

# Function to trigger the alarm
def alarm(task):
    print(f"\n🚨 Reminder! Time to do: '{task}'")

# Simple CLI for interacting with the To-Do list
def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions: ")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task: ")
            reminder_choice = input("Do you want to set a reminder? (yes/no): ").lower()
            if reminder_choice == "yes":
                due_time_str = input("Enter the reminder time (YYYY-MM-DD HH:MM:SS): ")
                todo_list.add_task(task, due_time_str)
                set_reminder(task, due_time_str)
            else:
                todo_list.add_task(task)
        elif choice == "2":
            todo_list.show_tasks()
        elif choice == "3":
            todo_list.show_tasks()
            task_number = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_number)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
