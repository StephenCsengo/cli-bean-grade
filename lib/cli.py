#!/usr/bin/env python3
from helper import menus


class Cli:
    def __init__(self):
        self.current_user = None

    # First screen the user sees
    def entry(self):
        print("    ____                   ______               __   ")
        print("   / __ )___  ____ _____  / ____/________ _____/ /__ ")
        print("  / __  / _ \/ __ `/ __ \/ / __/ ___/ __ `/ __  / _ \ ")
        print(" / /_/ /  __/ /_/ / / / / /_/ / /  / /_/ / /_/ /  __/")
        print("/_____/\___/\__,_/_/ /_/\____/_/   \__,_/\__,_/\___/ ")

        print(
            "\n\nWelcome to BeanGrade!\n"
            "Keep track of all of the specialty coffees your household has tried.\n"
            "Start by logging in or creating a new user."
        )
        menus.main_menu(self)


if __name__ == "__main__":
    app = Cli()
    app.entry()
