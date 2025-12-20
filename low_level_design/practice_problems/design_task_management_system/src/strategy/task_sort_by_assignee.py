"""Sort the task by assignee"""

from strategy.task_sort_strategy import TaskSortStrategy

class SortByAssignee(TaskSortStrategy):
    """different version of sort if we don't use lambda function, avoid using tasks.sort() because it can modify the existing list and sorted() returns new list"""
    def sort(self, tasks):
        return sorted(tasks, key=self._assignee_key)

    def _assignee_key(self, task):
        return task.assignee.name if task.assignee else ""
