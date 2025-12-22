"""Class to print or display all the tasks"""
from core.task import Task
from core.task_list import TaskList

class DisplayTasks:
    @staticmethod
    def display_task(task: Task):
        print(f"---{task.id}|"
              f"---{task.title}|"
              f"Status: {task.status.value} | "
              f"Priority: {task.priority.label} | "
              f"Assignee: {task.assignee.name if task.assignee else 'Unassigned'}"

              )
        
    @staticmethod
    def display_task_list(task_list:TaskList):
        print(f"\n===== Task List: {task_list.name} =====")
        for task in task_list.get_tasks():
            DisplayTasks.display_task(task)
        print("=====================================\n")