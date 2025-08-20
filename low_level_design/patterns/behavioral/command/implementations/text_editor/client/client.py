"""client runner implementation"""
from commands import *
from core.text_editor import TextEditor
from core.command_manager import CommandManager
def run_text_editor_command():

    print("\nRunning text editor for command design pattern")

    text_editor = TextEditor()
    command_manager = CommandManager()
    
    # Step 1: Insert text
    insert_command = InsertTextCommand(
        text_editor,
        "Hello! welcome to system design repository for command design pattern"
    )
    command_manager.set_command(insert_command)
    command_manager.run_command()
    print("After Insert:", text_editor.show_content())
    
    # Step 2: Delete text
    delete_command = DeleteTextCommand(text_editor, start=7, length=4)
    command_manager.set_command(delete_command)
    command_manager.run_command()
    print("After Delete:", text_editor.show_content())
    
    # Step 3: Cut text
    cut_command = CutCommand(text_editor, start=8, length=3)
    command_manager.set_command(cut_command)
    command_manager.run_command()
    print("After Cut:", text_editor.show_content())
    
    # Step 4: Undo last command (Cut)
    command_manager.undo()
    print("After Undo (Cut):", text_editor.show_content())
    
    # Step 5: Undo previous command (Delete)
    command_manager.undo()
    print("After Undo (Delete):", text_editor.show_content())
    
    # Step 6: Redo last undone command (Delete)
    command_manager.redo()
    print("After Redo (Delete):", text_editor.show_content())
    
    # Step 7: Paste (from clipboard)
    paste_command = PasteCommand(text_editor, position=5)
    command_manager.set_command(paste_command)
    command_manager.run_command()
    print("After Paste:", text_editor.show_content())
    
    # Step 8: Undo Paste
    command_manager.undo()
    print("After Undo (Paste):", text_editor.show_content())

    # Step 9: Copy command
    copy_command=CopyCommand(text_editor, 5, 9)
    command_manager.set_command(copy_command)
    command_manager.run_command()

    print("After Copy content in clipboard=",text_editor.clipboard)

    paste_command = PasteCommand(text_editor, position=5)
    command_manager.set_command(paste_command)
    command_manager.run_command()
    print("After Paste:", text_editor.show_content())




    