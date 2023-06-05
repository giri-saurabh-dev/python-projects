from asyncio import Task
from datetime import datetime

class UserInterface:
    def __init__(self, todo_list):
        self.todo_list = todo_list

    def print_menu(self):
        print("1. Add a task")
        print("2. Mark a task as complete")
        print("3. Sort tasks by due date")
        print("4. Filter tasks by completion status")
        print("5. Save tasks to file")
        print("6. Load tasks from file")
        print("7. Exit")

    def run(self):
        while True:
            self.print_menu()
            choice = input("Enter your choice (1-7): ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.mark_task_complete()
            elif choice == "3":
                self.sort_tasks_by_due_date()
            elif choice == "4":
                self.filter_tasks_by_completion_status()
            elif choice == "5":
                self.save_tasks_to_file()
            elif choice == "6":
                self.load_tasks_from_file()
            elif choice == "7":
                break
            else:
                print("Invalid choice. Please try again.")

    def add_task(self):
        task_id = input("Enter the task ID: ")
        title = input("Enter the task title: ")
        print("Enter the due date in the format YYYY-MM-DD (e.g., 2023-06-10)")
        while True:
            due_date_input = input("Enter the due date (optional): ")
            if not due_date_input:
                due_date = None
                break
            try:
                due_date = datetime.strptime(due_date_input, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid date format. Please try again.")
        task = Task(task_id, title, due_date=due_date)
        self.todo_list.add_task(task)
        print("Task added successfully.")

    def mark_task_complete(self):
        task_id = input("Enter the task ID to mark as complete: ")
        self.todo_list.mark_task_complete(task_id)
        print("Task marked as complete.")

    def sort_tasks_by_due_date(self):
        self.todo_list.sort_tasks_by_due_date()
        print("Tasks sorted by due date.")

    def filter_tasks_by_completion_status(self):
        is_completed = input("Enter the completion status (True/False): ")
        filtered_tasks = self.todo_list.filter_tasks_by_completion_status(is_completed)
        print("Filtered tasks:")
        for task in filtered_tasks:
            print(task.title)

    def save_tasks_to_file(self):
        file_path = input("Enter the file path to save tasks: ")
        self.todo_list.save_tasks_to_file(file_path)
        print("Tasks saved to file.")

    def load_tasks_from_file(self):
        file_path = input("Enter the file path to load tasks from: ")
        self.todo_list.load_tasks_from_file(file_path)
        print("Tasks loaded from file.")
