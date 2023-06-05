class Task:
    def __init__(self, task_id, title, is_completed=False, due_date=None):
        self.task_id = task_id
        self.title = title
        self.is_completed = is_completed
        self.due_date = due_date
