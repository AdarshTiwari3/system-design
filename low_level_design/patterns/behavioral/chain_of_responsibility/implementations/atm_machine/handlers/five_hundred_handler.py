"""500 Rs handler implementation"""

from core.base_handler import BaseHandler

class FiveHundredHandler(BaseHandler):
    def handle(self, request):
        
        if request.amount>=500:
            notes=request.amount//500
            request.amount%=500

            print(f"\n[Dispensing]- {notes} x 500 notes")

        self.handle_next(request)