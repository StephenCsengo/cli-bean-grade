from simple_term_menu import TerminalMenu

from models import User, Coffee, session
from prettytable import PrettyTable


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
            options = ["Show All Coffees", "Show My Ratings", "Search For A Coffee"]
            terminal_menu = TerminalMenu(options)
            menu_index = terminal_menu.show()

            if options[menu_index] == "Show All Coffees":
                show_all_coffees = session.query(Coffee).all()
                table = PrettyTable()

                table.field_names = ["ID", "Roaster", "Name", "Roast Level"]

                for coffee in show_all_coffees:
                    table.add_row(
                        [coffee.id, coffee.roaster, coffee.name, coffee.roast_level]
                    )

                print(self.current_user)
                print(table)

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
