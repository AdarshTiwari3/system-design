#client code 
from factories.gui_factory import GUIFactory
def render_gui(factory: GUIFactory):

    button=factory.create_button()
    checkbox=factory.create_checkbox()

    print(button.render())
    print(checkbox.render())

    button.on_click(lambda:print("Button Clicked!"))
    def checkbox_msg():
        print("CheckBox checked!")

    checkbox.on_check(checkbox_msg)

    button.simulate_click()
    checkbox.simulate_check()
    

    

    
