from builder.create_house_builder import CreateHouseBuilder
from director.director import ConstructionDirector
def run_builder_method():


    #director is optional method we can also construct the house using CreateBuilder
    builder = CreateHouseBuilder() 
    house1=builder.set_walls(True).set_roof(True).set_windows(False).build()
    print(house1)
    director = ConstructionDirector(builder)  # ✅ abstraction injected- Dependency Inversion Principle (DIP) means rather than call subclass we call abstract so it can be loosly coupled also

    house2 = director.construct_luxury_house()
    print(house2)  # Output: House with: Walls, Doors, Windows

if __name__ == "__main__":
    print("\nBuilder Design Pattern")
    run_builder_method()
