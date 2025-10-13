# David Wylie
# CIS256 24903
# Programming Assignment 3 (PA 3)
# Execise 2: Deque in Action
# I reused logic from the EMS and list manipulation programs

from collections import deque


class Task:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return f"{self.name}"


class Task_List:
    def __init__(self):
        self._tasks = deque()

    # Dunders for deque manipulation
    def __len__(self):
        return len(self._tasks)

    def __iter__(self):
        return iter(self._tasks)

    # Deque methods to carry out tasks.
    def append(self, task_name):
        new_task = Task(task_name)
        self._tasks.append(new_task)
        print(f"{new_task.name} added to the back")

    def appendleft(self, task_name):
        new_task = Task(task_name)
        self._tasks.appendleft(new_task)
        print(f"{new_task.name} added to the front")

    def pop(self):
        if not self._tasks:
            print("No tasks to pop!")
            return
        task = self._tasks.pop()
        print(f"{task.name} completed (popped from back)")
        return task

    def popleft(self):
        if not self._tasks:
            print("No tasks to pop!")
            return
        task = self._tasks.popleft()
        print(f"{task.name} completed (popped from front)")
        return task

    def clear(self):
        return self._tasks.clear()

    def __str__(self):
        if not self._tasks:
            return "Task List:\n(empty)\n"
        tasks = '\n'.join(
            f"{i}. {task}" for i, task in enumerate(self._tasks, 1)
            )
        return (
            f"Task List: {len(self._tasks)} Tasks\n"
            f"{'-' * 16}\n{tasks}\n"
        )


def user_interface(task_list):
    """
        Helper function to interact with task objects in the
        task list object and demonstrate DEQUE IN ACTION!
        :params: task list object
        :return: None, Uses all helper functions to interact with task list
    """
    # Main program loop - continues until user chooses to exit
    while True:
        try:
            print("""
Select from the Following Options
    1. View all Tasks
    2. Pop a Task (Back)
    3. Popleft a Task (Front)
    4. Append a Task (Back)
    5. Appendleft a Task (Front)
    6. Exit Application
                  """)

            response = int(input("Enter Option: "))
            match response:
                case 1:
                    print(task_list)
                case 2:
                    task_list.pop()
                case 3:
                    task_list.popleft()
                case 4:
                    task_list.append(
                        str(input("Enter a Task: "))
                    )
                case 5:
                    task_list.appendleft(
                        str(input("Enter a Task: "))
                    )
                case 6:
                    print("Goodbye!")
                    exit()
                case _:
                    print("Please Enter a Number from 1 to 6.")
        except ValueError:
            print("Error: Please enter a valid integer.")


def main():
    print("IT'S TIME TO SEE DEQUES IN ACTION!!!")
    task_list = Task_List()

    # Tasks Entered to show deque in ACTION!
    task_list.append('shopping')
    task_list.appendleft('meeting')
    task_list.append('karate')
    task_list.appendleft('nap')
    task_list.append("lunch")

    user_interface(task_list)


main()
