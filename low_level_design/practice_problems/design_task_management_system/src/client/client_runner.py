"""Client Runner"""
from core.task_service import TaskService
from observer.activity_observer import ActivityObserver
from entities.user import User
from core.task_list import TaskList
from core.task import Task
from enums.task_priority import TaskPriority
from views.display_tasks import DisplayTasks
from strategy.task_sort_by_priority import SortByPriority

def main():
    print("\n=== Task Management System Demo ===\n")
    # 1. create task service and attach an observer to this
    task_service=TaskService()

    activity_logger=ActivityObserver()

    task_service.add_observer(activity_logger)

    # 2. create user
    andy=User("Andy Romio", "andy-romio@gmail.com")
    johndoe=User("John Doe", "johndoe@gmail.com")

    # 3. create task list

    sprint_task=TaskList("Sprint Backlog")

     # 4. Create tasks

    task1=Task(title="Design Task Management System",
            description="Create clean LLD with SOLID principles",
            priority=TaskPriority.HIGH, assignee=andy)

    task2 = Task(
        title="Implement Optimistic Locking",
        description="Prevent concurrent update issues",
        priority=TaskPriority.CRITICAL,
        assignee=johndoe
    )

    # 5. Add tasks to task list

    sprint_task.add_task(task1)
    sprint_task.add_task(task2)

    print("------Initial Tasks-----")

    DisplayTasks.display_task_list(sprint_task)

    # 7. Start task1

    expected_version = task1.version

    task_service.start(task1, expected_version)

    print("After starting Task 1:")
    DisplayTasks.display_task_list(sprint_task)

    expected_version = task1.version
    task_service.complete(task1, expected_version)

    print("After completing Task 1:")
    DisplayTasks.display_task_list(sprint_task)

    # 8. Demonstrate optimistic locking failure
   
    print("Demonstrating optimistic locking failure:")
    stale_version = task2.version
    task_service.start(task2, stale_version) # valid update

    print("\n After Task 2 started the Tasks:")

    DisplayTasks.display_task_list(sprint_task)

    try:
        # Using Old version intentionally to simulate failure
        task_service.complete(task2, stale_version)
    except RuntimeError as e:
        print(f"Expected error: {e}")

    # 9. all done

    print("\nFinal Tasks:")

    sorting_strategy=SortByPriority()
    DisplayTasks.display_task_list(sprint_task, sorting_strategy)

    print("\n=== Demo Completed ===\n")





   
