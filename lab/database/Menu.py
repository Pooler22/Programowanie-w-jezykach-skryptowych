from lab.database.Option import *
from lab.database.AutoIncrement import AutoIncrement


class Menu(AutoIncrement):
    def __init__(self):
        self.options = []
        self.ai = AutoIncrement.auto_increment()

    def print(self):
        [print(option) for option in self.options]

    def add_option(self, text, function):
        self.options.append(Option(self.ai.__next__(), text, function))
