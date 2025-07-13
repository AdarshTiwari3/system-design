

"""
Difference between Shallow Copy and Deep Copy:

1. Shallow Copy:
   - Creates a new outer object.
   - Copies references of nested (inner) mutable objects.
   - Result: Changes made to nested objects in the copy will reflect in the original.
   - Function: copy.copy(obj)

2. Deep Copy:
   - Creates a new outer object AND recursively copies all nested objects.
   - Result: The copy is fully independent from the original.
   - Function: copy.deepcopy(obj)

Example:

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

shallow[0][0] = 99
deep[1][1] = 88

print("Original:", original)     # [[99, 2], [3, 4]] — affected by shallow copy
print("Shallow:", shallow)       # [[99, 2], [3, 4]]
print("Deep:", deep)             # [[1, 2], [3, 88]] — fully independent

"""
import copy
from prototype import Prototype
from typing_extensions import Self, Dict

class Document(Prototype):
    def __init__(self, title, content, metadata):
        self._title: str = title
        self._content: str = content
        self._metadata: dict = metadata  # dict, mutable

    def set_title(self, title: str):
        if not title.strip():
            raise ValueError("Title cannot be empty")
        self._title = title

    def set_content(self, content: str):
        self._content = content

    def set_metadata(self, metadata: Dict):
        if not isinstance(metadata, dict):
            raise TypeError("Metadata must be a dictionary")
        self._metadata = metadata


    def clone(self) -> Self:
        return copy.deepcopy(self)

    def __str__(self):
        return f"Title: {self._title}\nContent: {self._content}\nMeta: {self._metadata}"
