"""
Product class for the Builder Design Pattern.

This class represents a URL composed of various parts. It will be constructed
incrementally using a builder.

A URL can consist of the following components:

1. Protocol (scheme):    e.g., "https" or "http"
2. Domain (host):        e.g., "google.com"
3. Port (optional):      e.g., 8080
4. Path (optional):      e.g., "/home"
5. Query Parameters:     e.g., userId="user_1", passed as key-value pairs

here we have some optional and required attributes so here chaining of method would be helpful so we will use builder design pattern as it delivers the same thing
Final Output Example:
    https://google.com:8080/home?userId=user_1

"""
