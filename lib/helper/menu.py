from simple_term_menu import TerminalMenu
from prettytable import PrettyTable
from models import User, Coffee, Rating, session
from helper import tables


def user_menu(self, current_user):
    print(f"Welcome {current_user.name}!")
    options = [
        "Show All Coffees",
        "Show My Ratings",
        "Search",
        "Add A New Coffee",
    ]
    terminal_menu = TerminalMenu(options)
    menu_index = terminal_menu.show()

    # Handle showing all coffees
    if options[menu_index] == "Show All Coffees":
        show_all_coffees = session.query(Coffee).all()

        tables.all_coffees(show_all_coffees)

    # Handle showing a user's rating
    elif options[menu_index] == "Show My Ratings":
        user_ratings = session.query(Rating).filter_by(user_id=self.current_user).all()

        tables.all_ratings(user_ratings)

    elif options[menu_index] == "Search":
        pass

    elif options[menu_index] == "Add A New Coffee":
        new_roaster = input("Enter the roaster: ")
        new_name = input("Enter the coffee's name: ")
        new_roast_level = input("Enter the roast level: ")
        new_coffee = {
            "roaster": new_roaster,
            "name": new_name,
            "roast_level": new_roast_level,
        }

        print(new_coffee["roaster"])
