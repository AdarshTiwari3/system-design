"""main method of abstract factory example of gui factory"""
from factories.mac_os_factory import MacOSFactory
from factories.windows_factory import WindowsFactory
from client.app import render_gui
def main():
    factories={
        "Windows": WindowsFactory(),
        "MacOS": MacOSFactory()
    }

    os_type=input("Enter Operating System Type: ").strip() #this will remove any space or other things like \n \t or other things
    factory=factories.get(os_type)
    if factory:
        render_gui(factory)
    else:
        raise ValueError("OS type is not supported")

if __name__=="__main__":
    print("\nImplementation of Abstract Factory Design Pattern")
    main()