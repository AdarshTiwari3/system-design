"""Client Runner"""
from originators.text_editor_originator import TextEditor
from caretaker.caretaker import History

def run_editor_memento():
    print(f"\nRunning text editor memento")

    editor=TextEditor()
    history=History()

    editor.write("Hello Memento")
    history.save(editor.save())

    editor.write(" I am an Editor Memento Implementation")
    history.save(editor.save())

    print(f"\nCurrent content={editor.get_content()}")

    editor.restore(history.undo())

    print(f"\nAfter Undo 1 , content={editor.get_content()}")

    editor.restore(history.undo())

    print(f"\nAfter Undo 2 , content={editor.get_content()}")

    
    editor.restore(history.undo())

    print(f'\nRedo last operation')
    editor.restore(history.redo())
    print(f"\nAfter Redo 1, content={editor.get_content()}")

    print(f'\nRedo last operation')
    editor.restore(history.redo())

    print(f"\nAfter Redo 2, content={editor.get_content()}")
    editor.restore(history.redo())