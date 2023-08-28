from simple_term_menu import TerminalMenu
from prettytable import PrettyTable
from models import User, Coffee, Rating, session
from helper import menu


def main_menu(self):
    def handle_login(self):
        name = input("Enter your name: ")
        user_search = User.find_by_name(name)
        self.current_user = user_search.id
        if user_search:
            menu.user_menu(self, current_user=user_search)

        else:
            print("User not found.")

    def handle_new_user(self):
        name = input("Please enter your name: ")
        User.add_new_user(name=name)
        new_user = User.find_by_name(name)
        self.current_user = new_user.id
        menu.user_menu(self, current_user=new_user)

    # def user_menu(self):

    def exit(self):
        print(
            "    (  )   (   )  )\n"
            "     ) (   )  (  (\n"
            "     ( )  (    ) )\n"
            "     _____________\n"
            "    <_____________> ___\n"
            "    |             |/ _ \ \n"
            "    |               | | |\n"
            "    |               |_| |\n"
            " ___|             |\___/\n"
            "/    \___________/    \ \n"
            "\_____________________/\n"
            "Enjoy your coffee!"
        )

    options = ["Login", "Create New User", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_index = terminal_menu.show()

    # Handle menu selections
    if options[menu_index] == "Login":
        handle_login(self)
    elif options[menu_index] == "Create New User":
        handle_new_user(self)
    else:
        exit(self)
