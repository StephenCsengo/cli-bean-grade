from simple_term_menu import TerminalMenu
from prettytable import PrettyTable
from models import User, Coffee, Rating, session
from helper import tables, forms


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
        forms.add_coffee(self)
        new_rating = input("Would you like to rate the new coffee? (Y/N):")
        if new_rating == "Y" or new_rating == "y":
            new_coffee = session.query(Coffee).order_by(Coffee.id.desc()).first()
            forms.add_rating(self, coffee_id=new_coffee.id)
            user_menu(self, current_user)
        else:
            user_menu(self, current_user)

    # Handle showing all coffees
    elif options[menu_index] == "Show All Coffees":
        show_all_coffees = session.query(Coffee).all()

        tables.all_coffees(show_all_coffees)
        mini_menu(self, current_user=current_user)

    # Handle showing a user's rating
    elif options[menu_index] == "Show My Ratings":
        user_ratings = session.query(Rating).filter_by(user_id=self.current_user).all()

        tables.all_ratings(user_ratings)
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
