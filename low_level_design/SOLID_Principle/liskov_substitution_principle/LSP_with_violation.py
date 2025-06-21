from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def fly(self) -> str:
        pass

class Sparrow(Bird):
    def fly(self) -> str:
        return "Sparrow can fly"

class Eagle(Bird):
    def fly(self) -> str:
        return "Eagle can fly"

class Ostrich(Bird):
    def fly(self) -> str:
        #this violates the property of LSP , bacause this will violate the property of BIRD class
        raise NotImplementedError("This voilates the property of LSP")
    


def can_fly(bird:Bird):
    print("Checking flying capability:")
    print(bird.fly())  # This will crash for Lion


#test function
can_fly(Sparrow()) 
can_fly(Eagle()) 
can_fly(Ostrich())