"""LogManager- singleton class"""
import threading
from typing import Dict, Self
from core.logger import Logger
class LogManager:
    _instance: 'LogManager | None'=None
    _lock=threading.Lock()

    def __init__(self):
        self.loggers: Dict[str, Logger]={}
        self.root_logger=Logger('root',None)
        self.loggers['root']=self.root_logger

    @classmethod
    def get_instance(cls) -> Self:
        """Thread safe singleton"""
        if cls._instance is None:
            with cls._lock: 
                if cls._instance is None:
                    cls._instance=LogManager()

        return cls._instance
    
    def get_logger(self, name: str) -> Logger:
        """Return existing logger or create a new one as a child of root."""
        if name in self.loggers:
            return self.loggers[name]

        logger = Logger(name, parent=self.root_logger)
        self.loggers[name] = logger
        return logger
    
    def get_root_logger(self) -> Logger:
        return self.root_logger
