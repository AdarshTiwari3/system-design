# Design a Task Management System

### Requirements

1. The system should allow users to create, update, and delete tasks

2. Each task should have a title, description, due date, priority, and status (e.g., pending, in progress, completed).

3. Users should be able to assign tasks to other users and set reminders

4. The system should support searching and filtering tasks by different criteria (e.g., priority, due date, assigned user)

5. Users should be able to mark tasks as completed and view task history

6. The system should handle concurrent access and ensure data consistency

7. The system should be extensible for future enhancements and new features


## Core Objects

1. **User**- Represents a system user who can create and be assigned tasks.

2. **TaskPriority (Enum)**- Defines the priority level of a task (LOW, MEDIUM, HIGH, CRITICAL).

3. **TaskStatus (Enum)**- Represents the current lifecycle state of a task (PENDING, IN_PROGRESS, BLOCKED, COMPLETED).

4. **Task**- Represents a single unit of work with all task-related information.

5. **TaskService**- Handles task workflows, assignments, and valid state transitions.

6. **TaskList**- Manages a collection of tasks in a thread-safe manner.

7. **TaskObserver**- Defines an interface to react to task-related events.

8. **ActivityObserver**- Tracks task changes and records task activity.

9. **ActivityLog**- Represents a history record of task-related actions.

10. **Search / Sort Strategy**- Provides different ways to search and filter tasks i.e due date, priority and assignee.

---

## Design Principles Used

- Single Responsibility Principle (SRP)
- Open/Closed Principle (OCP)
- Observer Pattern
- Strategy Pattern
- Optimistic Locking
- Task states are managed using a simple state machine rather than the State design pattern.

