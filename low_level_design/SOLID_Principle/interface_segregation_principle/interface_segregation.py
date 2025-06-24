'''
Interface Segregation Principle- No client should be forced to depend on interfaces they don't use. or Clients should not be forced to depend on methods that they do not use.
In simpler terms:
-Don't create large, bloated interfaces.
-Instead, break them down into smaller, more specific interfaces so that classes only need to implement the methods that are relevant to them.

---------------------------------------------------------------------------------------------------------
Benefits of ISP- 

- Promotes high cohesion and low coupling.

- Makes systems easier to refactor and extend.

- Improves readability and maintainability.

- Reduces the impact of changes in the codebase.

***The main idea behind ISP is to prevent the creation of "fat" or "bloated" interfaces that include methods that are not required by all clients.***

'''

from abc import ABC, abstractmethod

# Interface definition

class Fax(ABC):
    @abstractmethod
    def fax(self) -> str:
        pass

class Printer(ABC):
    @abstractmethod
    def print(self) -> str:
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self) -> str:
        pass


# Implementation

class NormalPrinter(Printer):
    def print(self):
        return "printing in progress..."
    
class MultiFunctionPrinter(Fax,Printer,Scanner):
    def print(self):
        return "printing in progress..."
    
    def scan(self):
        return "scanning in progress..."
    
    def fax(self):
        return "fax in progress..."




# Client Code

def run_interface_segregation_principles() -> None:
    normal_printer=NormalPrinter()
    multi_feature_printer=MultiFunctionPrinter()

    print(f"normal printer's {normal_printer.print()}")
    print(multi_feature_printer.print())
    print(multi_feature_printer.fax())
    print(multi_feature_printer.scan())