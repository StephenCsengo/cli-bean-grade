from models import User, Coffee, Rating, session


def add_coffee(self):
    new_coffee = {
        "roaster": input("Enter the roaster: "),
        "name": input("Enter the coffee's name: "),
        "roast_level": input("Enter the roast level: "),
    }

    Coffee.add_new_coffee(
        roaster=new_coffee["roaster"],
        name=new_coffee["name"],
        roast_level=new_coffee["roast_level"],
    )


def add_rating(self, coffee_id):
    rating = get_rating(self)
    Rating.add_new_rating(user_id=self.current_user, coffee_id=coffee_id, rating=rating)


def edit_rating(self):
    all_ratings = Rating.get_all_ratings(self.current_user)
    all_rating_ids = []
    for rating in all_ratings:
        all_rating_ids.append(rating.id)

    id = int(input("Enter the ID of the rating you'd like to edit: "))
    while id not in all_rating_ids:
        id = int(
            input(
                "Entered ID is not valid. Enter the ID of the rating you'd like to edit: "
            )
        )
    rating = get_rating(self)
    Rating.update_rating(id=id, new_rating=rating)


def get_rating(self):
    rating = int(input("Rate this coffee 1-10: "))
    while rating < 1 or rating > 10:
        print("Rating must be between 1 and 10, please try again.")
        rating = int(input("Rate this coffee 1-10: "))
    return rating


def select_coffee(self):
    all_coffees = Coffee.get_all_coffees()
    all_coffee_ids = []
    for coffee in all_coffees:
        all_coffee_ids.append(coffee.id)

    selected_coffee = int(input("Enter the ID of the coffee you'd like to edit: "))
    while selected_coffee not in all_coffee_ids:
        selected_coffee = int(
            input(
                "Entered ID is not valid. Enter the ID of the coffee you'd like to edit: "
            )
        )
    return selected_coffee


def edit_roaster(self, coffee_id):
    new_roaster = input("Enter the new roaster name: ")
    Coffee.update_roaster(id=coffee_id, new_roaster=new_roaster)


def edit_coffee_name(self, coffee_id):
    new_name = input("Enter the new coffee name: ")
    Coffee.update_name(id=coffee_id, new_name=new_name)


def edit_roast_level(self, coffee_id):
    new_roast_level = input("Enter the new roast level: ")
    Coffee.update_roast_level(id=coffee_id, new_roast_level=new_roast_level)
