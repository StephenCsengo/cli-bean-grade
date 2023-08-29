from models import User, Coffee, Rating, session


def add_coffee(self):
    new_roaster = input("Enter the roaster: ")
    new_name = input("Enter the coffee's name: ")
    new_roast_level = input("Enter the roast level: ")
    new_coffee = {
        "roaster": new_roaster,
        "name": new_name,
        "roast_level": new_roast_level,
    }

    Coffee.add_new_coffee(
        roaster=new_coffee["roaster"],
        name=new_coffee["name"],
        roast_level=new_coffee["roast_level"],
    )
