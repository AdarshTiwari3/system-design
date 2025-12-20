# Design a Task Management System

### Requirements

1. The system should allow users to create, update, and delete tasks

2. Each task should have a title, description, due date, priority, and status (e.g., pending, in progress, completed).

3. Users should be able to assign tasks to other users and set reminders

4. The system should support searching and filtering tasks by different criteria (e.g., priority, due date, assigned user)

5. Users should be able to mark tasks as completed and view task history

6. The system should handle concurrent access and ensure data consistency

7. The system should be extensible for future enhancements and new features


### Core Objects

1. **User** - represents user class having details about id, name and email.

2. **TaskPriority**- Enum class of task priority as LOW, MEDIUM, HIGH etc.

3. **TaskStatus**- Enum class of task status i.e IN_PROGRESS, PENDING, COMPLETED etc.