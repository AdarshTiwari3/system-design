"""2000 Rs handler implementation"""
from core.base_handler import BaseHandler
class TwoThousandHandler(BaseHandler):
    def handle(self, request):
        
        if request.amount>=2000:
            notes=request.amount//2000
            request.amount%=2000

            print(f"\n[Dispensing] {notes} x 2000 notes")
        self.handle_next(request)