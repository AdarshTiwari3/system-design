"""Commands will be implemented here"""

from commands.copy_command import CopyCommand
from commands.cut_command import CutCommand
from commands.insert_command import InsertTextCommand
from commands.delete_command import DeleteTextCommand
from commands.paste_command import PasteCommand
__all__=[
'CopyCommand','CutCommand','InsertTextCommand','DeleteTextCommand', 'PasteCommand'
]