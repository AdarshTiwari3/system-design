# lets see the example where isp rule is violated


'''
ISP- A class should not be forced to implement interfaces it does not use

An interface is a contract that defines a set of methods a class must implement — without providing any implementation itself
like abstract class

In other words:
-Break big, general-purpose interfaces into smaller, role-specific ones.
-Let classes implement only what they actually need.


 ISP helps enforce SRP(single responsibilty) by splitting large interfaces into smaller ones, each with a single responsibility.

'''

from abc import ABC, abstractmethod

class Machine(ABC):
    @abstractmethod
    def print(self)-> str:
        pass

    @abstractmethod
    def fax(self):
        pass

    @abstractmethod
    def scan(self):
        pass


class SimplePrinter(Machine):
    def print(self):
        return "this can print, printing in progress..."
    
    def fax(self):
        raise NotImplementedError("it can't fax")
    
    def scan(self):
        raise NotImplementedError("it can't scan")
    

#this will violate the ISP as few features are not supported and unnecessary we are forcing

printer=SimplePrinter()

print(printer.print())
print(printer.fax()) #this violates ISP