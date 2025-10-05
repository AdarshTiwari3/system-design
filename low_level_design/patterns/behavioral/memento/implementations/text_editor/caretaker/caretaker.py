"""Caretaker: Stores and retrieves Mementos, history and perform undo operation"""
from memento.memento_base import MementoBase

class History:
    def __init__(self):
        self._history: list[MementoBase]=[]
        self._redo_stack: list[MementoBase]=[]

    def save(self, memento: MementoBase) -> None:
        self._history.append(memento)
        self._redo_stack.clear()

    def undo(self) -> MementoBase | None:
        if len(self._history)==0:
            print(f'\nNothing to undo')
            return None
        popped=self._history.pop()
        self._redo_stack.append(popped)
        return self._history[-1] if self._history else None
    
    def redo(self) -> MementoBase | None:
        if len(self._redo_stack)==0:
            print(f"\nNothing to redo")
            return None
        popped=self._redo_stack.pop()
        self._history.append(popped)
        return popped

