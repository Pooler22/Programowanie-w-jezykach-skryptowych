import sys

from lab.database.gui.Option import *

from lab.database.database.AutoIncrement import AutoIncrement
from lab.database.gui.AwesomeEffects import AwesomeEffects


class Menu(AutoIncrement):
    def __init__(self, description):
        self.description = description
        self.graphic = ""
        self.options = []
        self.ai = AutoIncrement.auto_increment(1)

    def add_graphic(self,graphic):
        self.graphic = graphic

    def init_menu(self):
        self.print()
        self.select_option()

    def print(self):
        print('{:#<258}'.format(''))
        AwesomeEffects.info(self.graphic)
        AwesomeEffects.info(self.description)
        [AwesomeEffects.info(str(option)) for option in self.options]

    def add_option(self, text, function):
        self.options.append(Option(self.ai.__next__(), text, function))

    def select_option(self):
        try:
            AwesomeEffects.info("Wpisz numer opcji( 0 -pomoc):")
            option_number = int(input())
            if option_number == 0:
                self.init_menu()
            elif option_number < self.options.__len__() + 1:
                AwesomeEffects.info("Wywołanie funkcji o numerze " + str(option_number))
                sys.stdin.flush()
                self.options.__getitem__(int(option_number-1)).function()
            else:
                sys.stdin.flush()
                AwesomeEffects.error("Nie ma opcji o takim numerze")
        except ValueError:
            AwesomeEffects.error("To nie jest numer")
        self.select_option()
