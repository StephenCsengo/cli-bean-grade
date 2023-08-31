from simple_term_menu import TerminalMenu
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
        mini_menu(self, current_user=current_user, append="coffees")

    # Handle showing a user's rating
    elif options[menu_index] == "Show My Ratings":
        handlers.handle_show_all_ratings(self)
        mini_menu(self, current_user=current_user)

    elif options[menu_index] == "Search":
        pass
    # Handle exit
    elif options[menu_index] == "Exit":
        handlers.handle_exit(self)


def mini_menu(self, current_user, append=None):
    if append == None:
        options = [
            "Back",
        ]
        terminal_menu = TerminalMenu(options)
        menu_index = terminal_menu.show()

        if options[menu_index] == "Back":
            user_menu(self, current_user)

    elif append == "coffees":
        options = [
            "Rate A Coffee",
            "Delete A Coffee",
            "Back",
        ]
        terminal_menu = TerminalMenu(options)
        menu_index = terminal_menu.show()

        if options[menu_index] == "Back":
            user_menu(self, current_user)

        elif options[menu_index] == "Rate A Coffee":
            handlers.handle_add_rating(self, current_user)

        elif options[menu_index] == "Delete A Coffee":
            handlers.handle_delete_coffee(self, current_user)


def main_menu(self):
    options = ["Login", "Create New User", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_index = terminal_menu.show()

    # Handle menu selections
    if options[menu_index] == "Login":
        handlers.handle_login(self)
    elif options[menu_index] == "Create New User":
        handlers.handle_new_user(self)
    else:
        handlers.handle_exit(self)
