"""Caretaker: Stores and retrieves Mementos, history and perform undo operation"""
from momento.momento_base import MomentoBase

class History:
    def __init__(self):
        self._history: list[MomentoBase]=[]
        self._redo_stack: list[MomentoBase]=[]

    def save(self, momento: MomentoBase) -> None:
        self._history.append(momento)
        self._redo_stack.clear()

    def undo(self) -> MomentoBase | None:
        if not self._history:
            print(f'\nNothing to undo')
            return None
        popped=self._history.pop()
        self._redo_stack.append(popped)
        return self._history[-1] if self._history else None
    
    def redo(self) -> MomentoBase | None:
        if not self._redo_stack:
            print(f"\nNothing to redo")
            return None
        popped=self._redo_stack.pop()
        self._history.append(popped)
        return popped

