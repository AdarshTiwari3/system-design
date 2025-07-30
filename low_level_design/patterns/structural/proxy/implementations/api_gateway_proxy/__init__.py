"""
This implementation demonstrates the Proxy Design Pattern using an API Gateway.

The API Gateway acts as a proxy that:
1. Intercepts incoming client requests,
2. Applies cross-cutting concerns like authentication, logging, and validation,
3. Forwards valid requests to the actual backend service (RealService).

This pattern helps decouple client access from backend logic while adding security and monitoring layers transparently.
"""
