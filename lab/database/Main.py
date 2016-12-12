import sys

sys.path.insert(1, "C:\\Users\\pooler\\PycharmProjects\\Programowanie-w-jezykach-skryptowych\\")
from time import gmtime, strftime
from random import randint
from asciimatics.screen import Screen
from lab.database.gui.Application import Application

app = Application()

print(strftime("%H:%M:%S", gmtime()))


def demo(screen):
    while True:
        screen.print_at('Dzień dobry Basiu!',
                        randint(0, screen.width), randint(0, screen.height),
                        colour=randint(0, screen.colours - 1),
                        bg=randint(0, screen.colours - 1))
        ev = screen.get_key()
        if ev in (ord(' '), ord('Q'), ord('q')):
            return
        screen.refresh()


Screen.wrapper(demo)
app.init()
