"""Task Sort by priority- LOW, MEDIUM, HIGH etc"""
from strategy.task_sort_strategy import TaskSortStrategy

class SortByPriority(TaskSortStrategy):

    def sort(self, tasks):
        """Sort the list tasks using a value extracted from each element by key
        [
        (task1, 1),
        (task2, 4),
        (task3, 3)
        ]
        reverse=True
        4 -> 3 -> 1

        [task2, task3, task1]
        sorted() returns a NEW list
        
        """

        return sorted(tasks, key=lambda task: task.priority.level, reverse=True)

       