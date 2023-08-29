from models import User, Coffee, Rating, session
from helper import tables, forms, menus


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
