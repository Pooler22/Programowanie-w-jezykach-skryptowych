import sys
from time import sleep

from colorama import init
init()
from colorama import Fore, Back, Style

class AwesomeEffects:
    @staticmethod
    def progres():
        for i in range(51):
            sys.stdout.write('\r')
            sys.stdout.write("%-50s %d%%" % ('\u2588' * i, 2 * i))
            sys.stdout.flush()
            sleep(0.03)
        sys.stdout.write('\n')

    @staticmethod
    def normal(text):
        sys.stdout.write(Fore.RED)
        print(text)
        sys.stdout.write(Fore.CYAN)

    @staticmethod
    def info(text):
        sys.stdout.write(Fore.RED)
        print(text)
        sys.stdout.write(Fore.CYAN)

    @staticmethod
    def succes(text):
        sys.stdout.write(Fore.RED)
        print(text)
        sys.stdout.write(Fore.CYAN)

    @staticmethod
    def error(text):
        sys.stdout.write(Fore.RED)
        print(text)
        sys.stdout.write(Fore.CYAN)

