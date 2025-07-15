"""Adapter Design Pattern Implementation:-
In the Adapter Design Pattern, there are two key components:

Adaptee: This is the existing or legacy interface that already provides certain functionality but does not match what the client expects.

Client: This is the component or system that expects a specific interface to interact with.

These two interfaces are incompatible and cannot communicate directly.
To resolve this mismatch, we introduce an Adapter, which acts as a bridge by converting the Adaptee's interface into the one the Client expects.
This enables seamless interaction without modifying either the Adaptee or the Client.


1. XML to JSON Converter

    Adaptee: XML format

    Client: Expects data in JSON

    Adapter: A parser or converter that transforms XML into JSON

2. Weight Machine: Pounds to Kilograms Converter

    Adaptee: Weight machine that returns weight in pounds (lbs)

    Client: Needs weight in kilograms (kg)

    Adapter: A converter that transforms pounds to kilograms before passing it to the client



"""