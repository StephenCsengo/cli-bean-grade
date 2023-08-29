from prettytable import PrettyTable
from models import User, Coffee, Rating, session


def all_coffees(coffees):
    table = PrettyTable()

    table.field_names = ["Coffee ID", "Roaster", "Name", "Roast Level"]

    for coffee in coffees:
        table.add_row([coffee.id, coffee.roaster, coffee.name, coffee.roast_level])

    print(table)


def all_ratings(ratings):
    table = PrettyTable()
    table.field_names = ["Rating ID", "Roaster", "Coffee", "Roast Level", "Rating"]

    for rating in ratings:
        table.add_row(
            [
                rating.id,
                rating.coffee.roaster,
                rating.coffee.name,
                rating.coffee.roast_level,
                rating.rating,
            ]
        )
    print(table)
