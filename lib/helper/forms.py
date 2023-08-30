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
    rating = int(input("Rate this coffee 1-10: "))
    while rating < 1 or rating > 10:
        print("Rating must be between 1 and 10, please try again.")
        rating = int(input("Rate this coffee 1-10: "))
    Rating.add_new_rating(user_id=self.current_user, coffee_id=coffee_id, rating=rating)
