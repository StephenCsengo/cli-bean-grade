from models import User, Coffee, Rating, session
from helper import tables, forms, menus
from helpers import main_menu


def handle_add_coffee(self, current_user):
    forms.add_coffee(self)
    new_rating = input("Would you like to rate the new coffee? (Y/N):")
    if new_rating == "Y" or new_rating == "y":
        new_coffee = session.query(Coffee).order_by(Coffee.id.desc()).first()
        forms.add_rating(self, coffee_id=new_coffee.id)
        menus.user_menu(self, current_user)
    else:
        menus.user_menu(self, current_user)


def handle_show_all_coffees(self):
    show_all_coffees = session.query(Coffee).all()
    tables.all_coffees(show_all_coffees)


def handle_show_all_ratings(self):
    user_ratings = session.query(Rating).filter_by(user_id=self.current_user).all()
    tables.all_ratings(user_ratings)


def handle_exit(self):
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


def handle_login(self):
    name = input("Enter your name: ")
    user_search = User.find_by_name(name)

    if user_search:
        self.current_user = user_search.id
        print(f"Welcome {user_search.name}!")
        menus.user_menu(self, current_user=user_search)

    else:
        create_new = input(
            "No user found. Would you like to create a new user? (Y/N): "
        )
        if create_new == "Y" or create_new == "y":
            handle_new_user(self)
        else:
            menus.main_menu(self)


def handle_new_user(self):
    name = input("Please enter your name: ")
    User.add_new_user(name=name)
    new_user = User.find_by_name(name)
    self.current_user = new_user.id
    menus.user_menu(self, current_user=new_user)
