# Design a Logger Framework

## Functional Requirements
1. Support multiple log levels: DEBUG, INFO, WARNING, ERROR, and FATAL.
2. Record each log entry with timestamp, log level, and message.
3. Allow multiple output destinations: console, file, and database.
4. Provide configuration for minimum log level and output destination.
5. Ensure thread safety for concurrent logging in multi-threaded contexts.
6. Support future extensibility for new log levels and output types.

## Identify Core Objects

1. **LogLevel** – Enum representing supported log severity levels (e.g., DEBUG, ERROR, FATAL).  

2. **LogMessage** – Represents a single log entry containing timestamp, level, message, logger name, and thread name.  

3. **LogFormatter** – Converts a LogMessage into a formatted output string. Implemented using the Strategy Pattern (e.g., JSON formatter, text formatter).  

4. **LogAppender** – Writes formatted logs to destinations such as console, file, or database.  

5. **Logger** – Creates log messages and routes them to configured appenders based on log level.  

6. **LogManager** – Singleton that manages loggers, maintains the root logger, and handles global configuration.

### Optional

7. **AsyncLogProcessor** – Optional component that processes log writes using a background thread to improve performance under high load.

---

## Design Patterns Used

1. **Singleton** – Used for creating and managing the global LogManager instance.  
2. **Strategy** – Used for interchangeable log formatters (JSON, text, etc.).