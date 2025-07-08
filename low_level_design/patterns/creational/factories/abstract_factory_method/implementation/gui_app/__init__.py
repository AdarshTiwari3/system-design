# implementation of GUI app using abstract factory here we have the following logics to be used-

"""
Product A, B:
- These are abstract product interfaces: `Button` and `Checkbox`.
- They define the common behavior for each UI component type.

Concrete A, B:
- These are the concrete implementations:
    → `WindowsButton`, `WindowsCheckbox`
    → `MacButton`, `MacCheckbox`

Abstract Factory:
- It is a "factory of factories".
- The `GUIFactory` interface defines factory methods like `create_button()` and `create_checkbox()` — without specifying the concrete subclasses.
- It allows creation of families of related UI components.

Concrete Factory:
- `WindowsFactory` and `MacOSFactory` are concrete factories.
- They implement the `GUIFactory` interface to return platform-specific components like `WindowsButton`, `MacCheckbox`, etc.
"""
