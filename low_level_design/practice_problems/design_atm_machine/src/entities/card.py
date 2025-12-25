"""Card- it will have card details"""

from datetime import date
class Card:
    def __init__(self, card_number: str, expiry_date: date):
        self._card_number=card_number
        self._expiry_date:date = expiry_date
      

    @property
    def card_number(self) -> str:
        return self._card_number
    
    @property
    def expiry_date(self) -> date:
        return self._expiry_date
    
    def is_expired(self) -> bool:
        return date.today() > self._expiry_date

    
