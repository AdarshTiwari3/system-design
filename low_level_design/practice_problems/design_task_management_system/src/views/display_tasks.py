"""Class to print or display all the tasks"""
from core.task import Task
from core.task_list import TaskList
from strategy.task_sort_strategy import TaskSortStrategy
from typing import Optional

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
    def display_task_list(task_list:TaskList, sort_strategy: Optional[TaskSortStrategy] = None):

        tasks = task_list.get_tasks(sort_strategy)
        
        print(f"\n===== Task List: {task_list.name} =====")
        for task in tasks:
            DisplayTasks.display_task(task)
        print("=====================================\n")