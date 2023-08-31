from simple_term_menu import TerminalMenu
from helper import tables, forms, handlers


def user_menu(self):
    options = [
        "Add A New Coffee",
        "Show All Coffees",
        "Add A New Rating",
        "Show My Ratings",
        "Exit",
    ]
    terminal_menu = TerminalMenu(options)
    menu_index = terminal_menu.show()

    # Handle adding a new coffee
    if options[menu_index] == "Add A New Coffee":
        handlers.handle_add_coffee(self)

    # Handle showing all coffees
    elif options[menu_index] == "Show All Coffees":
        handlers.handle_show_all_coffees(self)

    # Handle showing a user's rating
    elif options[menu_index] == "Show My Ratings":
        handlers.handle_show_all_ratings(self)

    # Handle exit
    elif options[menu_index] == "Exit":
        handlers.handle_exit(self)


def mini_menu(self, append=None):
    if append == None:
        options = [
            "Back",
        ]
        terminal_menu = TerminalMenu(options)
        menu_index = terminal_menu.show()

        if options[menu_index] == "Back":
            user_menu(self)

    elif append == "coffees":
        options = [
            "Edit A Coffee",
            "Rate A Coffee",
            "Delete A Coffee",
            "Back",
        ]
        terminal_menu = TerminalMenu(options)
        menu_index = terminal_menu.show()

        if options[menu_index] == "Back":
            user_menu(self)

        elif options[menu_index] == "Edit A Coffee":
            coffee_id = forms.select_coffee(self)
            edit_coffee_menu(self, coffee_id=coffee_id)

        elif options[menu_index] == "Rate A Coffee":
            handlers.handle_add_rating(self)

        elif options[menu_index] == "Delete A Coffee":
            handlers.handle_delete_coffee(self)

    elif append == "ratings":
        options = [
            "Edit A Rating",
            "Delete A Rating",
            "Delete All My Ratings",
            "Back",
        ]
        terminal_menu = TerminalMenu(options)
        menu_index = terminal_menu.show()

        if options[menu_index] == "Back":
            user_menu(self)

        elif options[menu_index] == "Edit A Rating":
            handlers.handle_update_rating(self)
            handlers.handle_show_all_ratings(self)

        elif options[menu_index] == "Delete A Rating":
            handlers.handle_delete_rating(self)

        elif options[menu_index] == "Delete All My Ratings":
            handlers.handle_delete_all_ratings(self)


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


def edit_coffee_menu(self, coffee_id):
    options = ["Edit Roaster", "Edit Name", "Edit Roast Level", "Back"]
    terminal_menu = TerminalMenu(options)
    menu_index = terminal_menu.show()

    if options[menu_index] == "Edit Roaster":
        handlers.handle_update_roaster(self, coffee_id=coffee_id)
    elif options[menu_index] == "Edit Name":
        handlers.handle_update_coffee_name(self, coffee_id=coffee_id)
    elif options[menu_index] == "Edit Roast Level":
        handlers.handle_update_roast_level(self, coffee_id=coffee_id)
    elif options[menu_index] == "Back":
        mini_menu(self, append="coffees")
