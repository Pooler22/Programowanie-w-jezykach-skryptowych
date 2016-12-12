import sys
from time import sleep
from colorama import init

init()
from colorama import Fore


class AwesomeEffects:
    def __init__(self, width):
        self.chromalog = None
        self.width = width

    def progress(self):
        for i in range(51):
            sys.stdout.write('\r')
            sys.stdout.write("%-10s %d%%" % ('\u2588' * i, 2 * i))
            sys.stdout.flush()
            sleep(0.03)
        sys.stdout.write('\n')

    def normal(self, text):
        sys.stdout.write(Fore.CYAN)
        sys.stdout.write('{:^250}'.format(text))
        sys.stdout.write(Fore.CYAN)

    def info(self, text):
        sys.stdout.write(Fore.BLUE)
        print("###\t\t\t" + '{:243}'.format(text) + "###")
        sys.stdout.write(Fore.CYAN)

    def line(self, text):
        sys.stdout.write(Fore.BLUE)
        print('{:#<243}'.format("#"))
        sys.stdout.write(Fore.CYAN)

    def succes(self, text):
        sys.stdout.write(Fore.GREEN)
        sys.stdout.write('{:^300}'.format(text))
        sys.stdout.write(Fore.CYAN)

    def error(self, text):
        sys.stdout.write(Fore.RED)
        sys.stdout.write('{:^300}'.format(text))
        sys.stdout.write(Fore.CYAN)
