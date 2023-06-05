from asyncio import Task


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.is_completed = True
                break

    def sort_tasks_by_due_date(self):
        self.tasks.sort(key=lambda task: task.due_date)

    def filter_tasks_by_completion_status(self, is_completed):
        return [task for task in self.tasks if task.is_completed == is_completed]

    def save_tasks_to_file(self, file_path):
        with open(file_path, 'w') as file:
            for task in self.tasks:
                file.write(f'{task.task_id},{task.title},{task.is_completed},{task.due_date}\n')

    def load_tasks_from_file(self, file_path):
        self.tasks = []
        with open(file_path, 'r') as file:
            for line in file:
                task_id, title, is_completed, due_date = line.strip().split(',')
                self.tasks.append(Task(task_id, title, is_completed=bool(is_completed), due_date=due_date))
