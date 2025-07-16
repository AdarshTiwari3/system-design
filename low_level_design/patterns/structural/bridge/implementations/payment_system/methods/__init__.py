"""Abstraction Folder"""

"""
Abstraction: Payment

This is the abstraction in the Bridge pattern. It defines the high-level
interface for processing payments and holds a reference to a Gateway
(implementor interface).

Why is Payment the Abstraction?
Because payments use gateways to process transactions — the abstraction
delegates the implementation of the actual transaction to the gateway.

Bridge Principle:
The Payment class bridges to the Gateway interface via composition,
allowing both to vary independently.
"""
