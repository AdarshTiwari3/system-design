# Design a Logger Framework

## Functional Requirements
1. Support multiple log levels: DEBUG, INFO, WARNING, ERROR, and FATAL.
2. Record each log entry with timestamp, log level, and message.
3. Allow multiple output destinations: console, file, and database.
4. Provide configuration for minimum log level and output destination.
5. Ensure thread safety for concurrent logging in multi-threaded contexts.
6. Support future extensibility for new log levels and output types.

## Identify Core Objects

1. **LogLevel**- enum for log levels i.e DEBUG, ERROR, WARNING and others

2. **LogMessage**- Represents a single log entry