from simple_term_menu import TerminalMenu
from prettytable import PrettyTable
from models import User, Coffee, Rating, session
from helper import menu


def main_menu(self):
    def handle_login(self):
        name = input("Enter your name: ")
        user_search = User.find_by_name(name)

        if user_search:
            self.current_user = user_search.id
            print(f"Welcome {user_search.name}!")
            menu.user_menu(self, current_user=user_search)

        else:
            create_new = input(
                "No user found. Would you like to create a new user? (Y/N): "
            )
            if create_new == "Y" or create_new == "y":
                handle_new_user(self)
            else:
                main_menu(self)

    def handle_new_user(self):
        name = input("Please enter your name: ")
        User.add_new_user(name=name)
        new_user = User.find_by_name(name)
        self.current_user = new_user.id
        menu.user_menu(self, current_user=new_user)

    options = ["Login", "Create New User", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_index = terminal_menu.show()

    # Handle menu selections
    if options[menu_index] == "Login":
        handle_login(self)
    elif options[menu_index] == "Create New User":
        handle_new_user(self)
    else:
        menu.exit(self)
