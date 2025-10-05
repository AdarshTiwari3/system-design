"""Client Runner"""
from handlers.two_thousand_handler import TwoThousandHandler
from handlers.five_hundred_handler import FiveHundredHandler
from handlers.hundred_handler import HundredHandler
from core.atm_service import ATMService

def build_chain():
    two_thousand = TwoThousandHandler()
    five_hundred = FiveHundredHandler()
    hundred = HundredHandler()

    two_thousand.set_next(five_hundred)
    five_hundred.set_next(hundred)

    return two_thousand



def run_atm():
    chain=build_chain()
    atm=ATMService(chain)

    print('\nWithdraw: 500')

    atm.withdraw(500)

    print('\nWithdraw: 3500')

    atm.withdraw(3500)

    print('\nWithdraw: 4600')

    atm.withdraw(4600)

    print('\nWithdraw: 3310')

    atm.withdraw(3310)
