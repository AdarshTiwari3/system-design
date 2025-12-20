"""Sort the task by due date"""

from strategy.task_sort_strategy import TaskSortStrategy

class SortByDueDate(TaskSortStrategy):
    def sort(self, tasks):
        return sorted(tasks, key= lambda task: task.due_date)