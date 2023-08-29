from simple_term_menu import TerminalMenu
from prettytable import PrettyTable
from models import User, Coffee, Rating, session
from helper import tables, forms


def user_menu(self, current_user):
    print(f"Welcome {current_user.name}!")
    options = [
        "Add A New Coffee",
        "Show All Coffees",
        "Add A New Rating",
        "Show My Ratings",
        "Search",
    ]
    terminal_menu = TerminalMenu(options)
    menu_index = terminal_menu.show()

    # Handle adding a new coffee
    if options[menu_index] == "Add A New Coffee":
        forms.add_coffee(self)
        new_rating = input("Would you like to rate the new coffee? (Y/N):")
        if new_rating == "Y":
            pass
        else:
            user_menu(self, current_user)

    # Handle showing all coffees
    elif options[menu_index] == "Show All Coffees":
        show_all_coffees = session.query(Coffee).all()

        tables.all_coffees(show_all_coffees)

    # Handle showing a user's rating
    elif options[menu_index] == "Show My Ratings":
        user_ratings = session.query(Rating).filter_by(user_id=self.current_user).all()

        tables.all_ratings(user_ratings)

    elif options[menu_index] == "Search":
        pass
