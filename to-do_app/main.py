from task import Task
from todo_list import TodoList
from user_interface import UserInterface

def main():
    todo_list = TodoList()
    user_interface = UserInterface(todo_list)
    user_interface.run()

if __name__ == "__main__":
    main()
