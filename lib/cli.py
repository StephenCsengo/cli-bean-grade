from simple_term_menu import TerminalMenu

from models import User, session


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
        if user_search:
            print(f"Welcome {user_search}!")
        else:
            print("User not found.")

    def handle_new_user(self):
        name = input("Please enter your name: ")
        user = User(name=name)
        session.add(user)
        session.commit()

    def exit(self):
        print("Enjoy your coffee!")


app = Cli()
app.entry()
