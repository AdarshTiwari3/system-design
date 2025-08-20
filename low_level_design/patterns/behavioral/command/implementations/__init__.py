"""
In the Command Design Pattern we have the following important components:

1. Invoker – Responsible for invoking the command.
   Example: A remote.

2. Command – Represents the action to be executed.

3. Receiver – The actual place where the command is executed.

4. Client – Does not know how the command is executed internally. 
   It only interacts with the Invoker to trigger the command.

Example: TV Remote

1. Invoker → TV Remote.
2. Client → User who presses a button to invoke the command.
3. When a button is pressed, a specific command is triggered and 
   passed to the Receiver (TV).
4. Commands can be stored in a history stack to support operations 
   like Undo (and Redo).

"""