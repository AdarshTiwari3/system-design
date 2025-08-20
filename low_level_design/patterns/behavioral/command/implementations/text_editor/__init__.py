"""
In the Command Design Pattern we have the following important components:

1. Invoker – Responsible for executing commands and managing their history.
   Example: CommandManager (handles execute, undo, redo).

2. Command – Represents an action to be performed.
   Example: InsertTextCommand, DeleteTextCommand.

3. Receiver – The actual object that performs the action.
   Example: TextEditor (executes insert and delete operations).

4. Client – Sets up the objects, creates commands, 
   and assigns them to the Invoker.
   Example: (wires editor, commands, and manager together).

Example: Text Editor with Undo/Redo

1. Invoker → CommandManager (manages execution and history of commands).
2. Client → The user who requests insert/delete operations.
3. When a user performs an action (insert/delete), a command is created 
   and executed by the Invoker, which delegates it to the Receiver (TextEditor).
4. Commands are stored in a history stack to support operations 
   like Undo (reverting an action) and Redo (reapplying an undone action).
"""
