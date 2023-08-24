from simple_term_menu import TerminalMenu

from models import User


class Cli:
    def __init__(self):
        self.current_user = None

    # First screen the user sees
    def entry(self):
        print("Welcome to BeanGrade!")
        options = ["Login", "Create New User", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_index = terminal_menu.show()

        # Handle menu selections
        if options[menu_index] == "Login":
            self.handle_login()
        elif options[menu_index] == "Create New User":
            self.handle_new_user()
        else:
            self.exit()

    def handle_login(self):
        name = input("Enter your name: ")

        print(name)

    def handle_new_user(self):
        name = input("Please enter your name: ")

        print(name)

    def exit(self):
        print("Enjoy your coffee!")


app = Cli()
app.entry()
