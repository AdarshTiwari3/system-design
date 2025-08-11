"""   
The Strategy pattern suggests that you take a class that does something specific in a lot of different ways and extract all of these algorithms into separate classes called strategies.

The original class, called context, must have a field for storing a reference to one of the strategies. The context delegates the work to a linked strategy object instead of executing it on its own.

Here in this example we have used- 

- Interface: Defines the common contract (AuthStrategy) for all authentication methods.
- Strategies: Concrete implementations of the interface (PasswordAuth, OAuthAuth, BiometricAuth).
- Context: Holds a reference to a strategy and delegates authentication to it (AuthContext).
- Client: Chooses and sets the strategy, then triggers authentication (UserService/main.py).


"""