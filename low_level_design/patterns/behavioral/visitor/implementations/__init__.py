"""
Visitor Design Pattern

Why Visitor and not Strategy?
- In Strategy, we separate and swap algorithms for the same behavior.
- In Visitor, we separate operations that apply to different object types.

Key Ideas:
- Elements (stable): Core classes like Paragraph, Image, Table.
- Visitors (evolving): New operations like Render, SpellCheck, Export.
- Double Dispatch: Element.accept(visitor) ensures the right operation
  is chosen based on both element type and visitor.
"""
