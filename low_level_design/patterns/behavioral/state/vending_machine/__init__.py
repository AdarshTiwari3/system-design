"""The State pattern suggests that you create new classes for all possible states of an object and extract all state-specific behaviors into these classes.
- Use the State pattern when you have an object that behaves differently depending on its current state, the number of states is enormous, and the state-specific code changes frequently.
- The pattern suggests that you extract all state-specific code into a set of distinct classes. As a result, you can add new states or change existing ones independently of each other, reducing the maintenance cost.

State Design Pattern - Vending Machine Example

The State pattern allows an object to change its behavior when its internal
state changes, making it appear as if the object has changed its class.

Components:
    1. State Interface
       - Defines a common contract for all vending machine states.
       - Concrete states (e.g., InitialState, ItemSelectedState,
         PaymentState, DispenseState) implement specific behaviors.

    2. Concrete States
       - Encapsulate the behavior for a particular state.
       - Handle requests and trigger transitions to other states
         by updating the context.

    3. Context (VendingMachine)
       - Maintains a reference to the current state.
       - Delegates all behavior to the current state object.
       - Provides a unified interface for the client while hiding
         state transition logic.

    4. Client
       - Interacts only with the Context (VendingMachine).
       - Is unaware of the state-specific classes or transitions.

State Flow (Vending Machine Example):
    InitialState → (item selected) → ItemSelectedState
    ItemSelectedState → (money inserted) → PaymentState
    PaymentState → (dispense action) → DispenseState
    DispenseState → (complete) → InitialState
"""