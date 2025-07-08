# implementation of factories 
"""
FactoryProvider – Super factory (also called factory of factories)
- Decides which concrete factory to return (e.g., WindowsFactory or MacOSFactory) based on input.
- Delegates object creation to the selected factory.

AbstractFactory – Interface for factories
- Defines abstract methods for creating related products (e.g., create_button, create_checkbox, create_menu).
- Ensures consistent interface across all concrete factories.

ConcreteFactories – Platform-specific factories (e.g., WindowsFactory, MacOSFactory)
- Implement the AbstractFactory interface.
- Responsible for creating concrete products like WindowsButton, MacCheckBox, etc.
"""
