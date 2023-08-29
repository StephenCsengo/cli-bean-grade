from simple_term_menu import TerminalMenu
from prettytable import PrettyTable
from models import User, Coffee, Rating, session
from helper import tables, forms, handlers


def user_menu(self, current_user):
    options = [
        "Add A New Coffee",
        "Show All Coffees",
        "Add A New Rating",
        "Show My Ratings",
        "Search",
        "Exit",
    ]
    terminal_menu = TerminalMenu(options)
    menu_index = terminal_menu.show()

    # Handle adding a new coffee
    if options[menu_index] == "Add A New Coffee":
        handlers.handle_add_coffee(self, current_user=current_user)
        mini_menu(self, current_user=current_user)
    # Handle showing all coffees
    elif options[menu_index] == "Show All Coffees":
        handlers.handle_show_all_coffees(self=self)
        mini_menu(self, current_user=current_user)

    # Handle showing a user's rating
    elif options[menu_index] == "Show My Ratings":
        handlers.handle_show_all_ratings(self)
        mini_menu(self, current_user=current_user)

    elif options[menu_index] == "Search":
        pass
    # Handle exit
    elif options[menu_index] == "Exit":
        exit(self)


def mini_menu(self, current_user):
    options = [
        "Back",
    ]
    terminal_menu = TerminalMenu(options)
    menu_index = terminal_menu.show()

    if options[menu_index] == "Back":
        user_menu(self, current_user)


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
