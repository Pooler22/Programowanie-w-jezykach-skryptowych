import sys

from lab.database.Option import *

from lab.database.database.AutoIncrement import AutoIncrement
from lab.database.gui.AwesomeEffects import AwesomeEffects


class Menu(AutoIncrement):
    def __init__(self):
        self.options = []
        self.ai = AutoIncrement.auto_increment(1)

    def print(self):
        [print(option) for option in self.options]

    def add_option(self, text, function):
        self.options.append(Option(self.ai.__next__(), text, function))

    def select_option(self):
        try:
            AwesomeEffects.info("Wpisz numer opcji:")
            option_number = int(input())
            if 0 < option_number < self.options.__len__() + 1:
                AwesomeEffects.info("Wywołanie funkcji o numerze " + str(option_number))
                self.options.__getitem__(int(option_number-1)).function()
            else:
                sys.stdin.flush()
                AwesomeEffects.error("Nie ma opcji o takim numerze")
        except ValueError:
            AwesomeEffects.error("To nie jest numer")
        self.select_option()
