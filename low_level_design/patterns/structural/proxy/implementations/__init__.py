"""Implementation of proxy design pattern
- Acts as a gatekeeper, delegating calls to the real object only when appropriate.
- Holds a reference to the real object and controls when and how it is created or accessed.
Proxy is a structural design pattern that lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.

The Proxy pattern suggests that you create a new proxy class with the same interface as an original service object. Then you update your app so that it passes the proxy object to all of the original object’s clients. Upon receiving a request from a client, the proxy creates a real service object and delegates all the work to it.
"""