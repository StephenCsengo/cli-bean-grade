from helpers import main_menu


class Cli:
    def __init__(self):
        self.current_user = None

    # First screen the user sees
    def entry(self):
        print("Welcome to BeanGrade!")
        main_menu(self)


app = Cli()
app.entry()
