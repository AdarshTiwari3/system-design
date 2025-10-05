"""Abstract Base Class for base handler so that we can avoid duplicating some commond operation across the handlers"""

from core.interface_handler import IHandler

class BaseHandler(IHandler):
    def __init__(self):
        self._next: IHandler = None

    def set_next(self, next_handler: IHandler):
        self._next=next_handler
        
        
    def handle_next(self,request):
        if self._next:
            self._next.handle(request)
        
