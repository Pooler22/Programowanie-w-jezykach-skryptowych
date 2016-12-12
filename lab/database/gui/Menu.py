import sys

from lab.database.gui.Option import *

from lab.database.database.AutoIncrement import AutoIncrement
from lab.database.gui.AwesomeEffects import AwesomeEffects


class Menu(AutoIncrement):
    def __init__(self, description, width=40):
        self.description = description
        self.awesome_effects = AwesomeEffects(width)

        self.graphic = ""
        self.options = []
        self.ai = AutoIncrement.auto_increment(1)

    def add_graphic(self, graphic):
        self.graphic = graphic

    def init_menu(self):
        self.print()
        self.select_option()

    def print(self):
        print('{:#<258}'.format(''))
        self.awesome_effects.info(self.graphic)
        self.awesome_effects.info(self.description)
        [self.awesome_effects.info(str(option)) for option in self.options]

    def add_option(self, text, function):
        self.options.append(Option(self.ai.__next__(), text, function))

    def select_option(self):
        try:
            self.awesome_effects.info("Wpisz numer opcji( 0 -pomoc):")
            option_number = int(input())
            if option_number == 0:
                self.init_menu()
            elif option_number < self.options.__len__() + 1:
                self.awesome_effects.info("Wywołanie funkcji o numerze " + str(option_number))
                sys.stdin.flush()
                self.options.__getitem__(int(option_number - 1)).function()
            else:
                sys.stdin.flush()
                self.awesome_effects.error("Nie ma opcji o takim numerze")
        except ValueError:
            self.awesome_effects.error("To nie jest numer")
        self.select_option()
