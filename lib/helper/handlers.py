from models import User, Coffee, Rating, session
from helper import tables, forms, menus


def handle_add_coffee(self):
    forms.add_coffee(self)
    new_rating = input("Would you like to rate the new coffee? (Y/N):")

    if new_rating == "Y" or new_rating == "y":
        new_coffee = Coffee.get_recent_coffee()
        forms.add_rating(self, coffee_id=new_coffee.id)
        menus.user_menu(self)

    else:
        menus.user_menu(self)


def handle_add_rating(self):
    if Coffee.get_all_coffees() == []:
        print("No coffees available to rate.")
        menus.mini_menu(self)
    else:
        coffee_choice = input("Enter the ID of the coffee you'd like to rate: ")
        forms.add_rating(self, coffee_id=coffee_choice)
        menus.user_menu(self)


def handle_show_all_coffees(self):
    all_coffees = Coffee.get_all_coffees()
    if all_coffees == []:
        print("No coffees to display. Try adding some.")
        menus.mini_menu(self)
    else:
        tables.all_coffees(all_coffees)
        menus.mini_menu(self, append="coffees")


def handle_show_all_ratings(self):
    all_user_ratings = Rating.get_all_ratings(user_id=self.current_user)
    if all_user_ratings == []:
        print("No ratings to display. Try rating some coffees.")
        menus.mini_menu(self)
    else:
        tables.all_ratings(all_user_ratings)
        menus.mini_menu(self, append="ratings")


def handle_delete_coffee(self):
    print(
        "\nWARNING! Deleting a coffee will also delete ratings associated with the coffee from all users.\n"
    )
    proceed = input("Do you wish to proceed? (Y/N): ")

    if proceed == "Y" or proceed == "y":
        coffee_id = input("Enter the ID of the coffee you'd like to delete: ")
        Coffee.delete_by_id(coffee_id=coffee_id)
        print("The coffee has been deleted.")

    handle_show_all_coffees(self)


def handle_delete_all_ratings(self):
    proceed = input("Are you sure you want to delete all of your ratings? (Y/N): ")

    if proceed == "Y" or proceed == "y":
        Rating.delete_by_user_id(user_id=self.current_user)
        print("All Ratings Deleted.")

    menus.user_menu(self)


def handle_delete_rating(self):
    rating = input("Enter the ID of the rating you'd like to delete: ")
    Rating.delete_by_rating_id(id=rating)
    print("Rating deleted.")
    handle_show_all_ratings(self)


def handle_update_rating(self):
    if Rating.get_all_ratings(user_id=self.current_user) == []:
        print("You haven't rated any coffees yet.")
        menus.mini_menu(self)
    else:
        forms.edit_rating(self)
        print("Rating updated!")


def handle_update_roaster(self, coffee_id):
    forms.edit_roaster(self, coffee_id=coffee_id)
    print("Roaster updated!")
    handle_show_all_coffees(self)


def handle_update_coffee_name(self, coffee_id):
    forms.edit_coffee_name(self, coffee_id=coffee_id)
    print("Coffee name updated!")
    handle_show_all_coffees(self)


def handle_update_roast_level(self, coffee_id):
    forms.edit_roast_level(self, coffee_id=coffee_id)
    print("Roast level updated!")
    handle_show_all_coffees(self)


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
        print(f"\nWelcome {user_search.name}!")
        menus.user_menu(self)

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
    menus.user_menu(self)
