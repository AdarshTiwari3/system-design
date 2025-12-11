"""Logger Implementation"""
from typing import Optional, List
from enums.log_level import LogLevel
from appenders.log_appender_interface import LogAppender
from core.log_message import LogMessage
class Logger:
    """The Logger creates log messages, while the Appender decides where those messages go."""

    def __init__(self, name: str, parent: Optional["Logger"] = None):
        """the parent is used to maintain a hierarchical tree of loggers, allowing child loggers to inherit log levels and appenders from their ancestors."""
        self.name=name #logger name
        self.parent=parent
        self.level: Optional[LogLevel] = None
        self.appenders: List[LogAppender] =[]
        #additivity refers to the behavior where log messages from a logger are forwarded to all appenders associated with that logger and its ancestors in the logger hierarchy"""
        self.additivity: bool=True #why True,  Child logger shares its logs with its parent.
        
        # this works like inheritance, few property we share from parent to reuse it and avoid re-configuartion
        # Additivity = True → log goes to child AND parent
        # Additivity = False → log goes to child only
        

    def set_level(self, level: LogLevel) -> None:
        self.level=level

    def add_appender(self, appender: LogAppender) -> None:
        self.appenders.append(appender)

    def get_appenders(self) -> List[LogAppender]:
        return self.appenders
    
    def set_additivity(self, additivity: bool):
        self.additivity=additivity

    def get_effective_level(self) -> LogLevel:
        """
        Resolve the effective log level by walking up the logger hierarchy.

        If this logger has no level set, it checks its parent, and so on.
        If no logger in the chain has a level set, default to DEBUG.
        """
        logger: Optional['Logger'] = self

        while logger:
            current_level=logger.level

            if current_level:
                return current_level
            logger=logger.parent

        return LogLevel.DEBUG #default root if nothing configured
    
    def log(self, level: LogLevel, message: str) -> None:
        """
        Log a message at the given level.

        The message is only logged if the given level is greater than or equal to
        the logger's effective level.
        """
        if not level.is_greater_or_equal(self.get_effective_level()):
            return 
        
        log_message=LogMessage(level,message,self.name)
        self._call_appenders(log_message)
        
    def _call_appenders(self, log_message: LogMessage): #for internal use only
        """It loops through all attached appenders (console, file, etc.), calls append() on each → log gets written"""
        for appender in self.appenders:
            appender.append(log_message)

        if self.additivity and self.parent:
            self.parent._call_appenders(log_message)

    def debug(self, message: str) -> None:
        self.log(LogLevel.DEBUG,message)

    
    def info(self, message:str) -> None:
        self.log(LogLevel.INFO, message)

    def warn(self, message: str) -> None:
        self.log(LogLevel.WARNING,message)

    def error(self, message: str) -> None:
        self.log(LogLevel.ERROR, message)

    def fatal(self, message: str) -> None:
        self.log(LogLevel.FATAL, message)



          
          

    
