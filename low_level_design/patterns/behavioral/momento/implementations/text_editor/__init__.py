"""
Text Editor with Undo/Redo using the Memento Design Pattern
===========================================================

This project demonstrates the **Memento Design Pattern** using a simple
text editor with undo/redo functionality.

- **Originator**: `TextEditor`
    Represents the object whose state needs to be saved and restored.
    In this case, the editor maintains the text content.

- **Memento**: `EditorMemento`
    Stores a snapshot of the `TextEditor`'s internal state at a
    given point in time without exposing implementation details.

- **Caretaker**: `History`
    Manages the list of saved mementos. Provides functionality to
    push (save) and pop (restore) states.

Why Memento Pattern?
--------------------
The Memento pattern is useful when:
- You need to save and restore object state without violating encapsulation.
- You want to provide undo/redo functionality.
- You want checkpointing or rollback mechanisms (e.g., transactions, games).

Real-World Applications
-----------------------
- **Text editors** (Undo/Redo functionality)
- **Games** (Saving checkpoints and restoring previous states)
- **Graphic editors** (Reverting to previous design state)
- **Database transactions** (Rollback to safe state)

Folder Structure
----------------
text_editor/
│── main.py                  # Client code (runs the demo)
│
├── originator/
│   └── text_editor.py        # Originator (TextEditor)
├── memento/
│   └── editor_memento.py     # Memento (EditorMemento)
├── caretaker/
│   └── history.py            # Caretaker (History)
└── tests/
    └── test_text_editor.py   # Unit tests


"""
