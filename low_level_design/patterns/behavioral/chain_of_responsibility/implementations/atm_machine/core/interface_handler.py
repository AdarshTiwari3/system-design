"""Handler Interface"""

from abc import ABC, abstractmethod

class IHandler(ABC):

    @abstractmethod
    def set_next(self,handler:'IHandler'):
        pass


    @abstractmethod
    def handle(self,request):
        pass