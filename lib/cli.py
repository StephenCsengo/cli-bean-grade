from simple_term_menu import TerminalMenu
from prettytable import PrettyTable
from models import User, Coffee, Rating, session


class Cli:
    def __init__(self):
        self.current_user = None

    # First screen the user sees
    def entry(self):
        print("Welcome to BeanGrade!")
        options = ["Login", "Create New User", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_index = terminal_menu.show()

        # Handle menu selections
        if options[menu_index] == "Login":
            self.handle_login()
        elif options[menu_index] == "Create New User":
            self.handle_new_user()
        else:
            self.exit()

    def handle_login(self):
        name = input("Enter your name: ")
        user_search = session.query(User).filter(User.name.like(name)).first()
        self.current_user = user_search.id
        if user_search:
            print(f"Welcome {user_search}!")
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
                table = PrettyTable()

                table.field_names = ["ID", "Roaster", "Name", "Roast Level"]

                for coffee in show_all_coffees:
                    table.add_row(
                        [coffee.id, coffee.roaster, coffee.name, coffee.roast_level]
                    )

                print(table)

            # Handle showing a user's rating
            elif options[menu_index] == "Show My Ratings":
                user_ratings = (
                    session.query(Rating).filter_by(user_id=self.current_user).all()
                )

                table = PrettyTable()
                table.field_names = ["Coffee", "Roast Level", "Rating"]

                for rating in user_ratings:
                    table.add_row(
                        [
                            f"{rating.coffee.roaster} {rating.coffee.name}",
                            rating.coffee.roast_level,
                            rating.rating,
                        ]
                    )
                print(table)

            elif options[menu_index] == "Search":
                pass

            elif options[menu_index] == "Add A New Coffee":
                pass

        else:
            print("User not found.")

    def handle_new_user(self):
        name = input("Please enter your name: ")
        user = User(name=name)
        session.add(user)
        session.commit()
        print(f"User {name} created.")

    # def user_menu(self):

    def exit(self):
        print("Enjoy your coffee!")


app = Cli()
app.entry()
