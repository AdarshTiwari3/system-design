"""100 Rs handler implementation"""

from core.base_handler import BaseHandler

class HundredHandler(BaseHandler):
    def handle(self, request):
        
        if request.amount>=100:
            notes=request.amount//100
            request.amount%=100

            print(f'\n[Dispensing]- {notes} x 100 notes')

        self.handle_next(request)