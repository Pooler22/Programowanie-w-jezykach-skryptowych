import sys
from random import randint
from asciimatics.screen import Screen

sys.path.insert(1, "C:\\Users\\208323.CARBON\\Desktop\\Programowanie-w-jezykach-skryptowych\\")
# sys.path.insert(1, "C:\\Users\\pooler\\PycharmProjects\\Programowanie-w-jezykach-skryptowych\\")
from lab.database.gui.Application import Application


def demo(screen):
    while True:
        screen.print_at('Dzień dobry Basiu! ',
                        randint(0, screen.width), randint(0, screen.height),
                        colour=randint(0, screen.colours - 1),
                        bg=randint(0, screen.colours - 1))
        ev = screen.get_key()
        if ev in (ord(' '), ord('Q'), ord('q')):
            return
        screen.refresh()


# Screen.wrapper(demo)

app = Application()
app.init()
