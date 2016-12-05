import sys
from time import sleep
from colorama import init

init()
from colorama import Fore


class AwesomeEffects:
    @staticmethod
    def progress():
        for i in range(51):
            sys.stdout.write('\r')
            sys.stdout.write("%-50s %d%%" % ('\u2588' * i, 2 * i))
            sys.stdout.flush()
            sleep(0.03)
        sys.stdout.write('\n')

    @staticmethod
    def normal(text):
        sys.stdout.write(Fore.CYAN)
        sys.stdout.write('{:^250}'.format(text))
        sys.stdout.write(Fore.CYAN)

    @staticmethod
    def info(text):
        sys.stdout.write(Fore.BLUE)
        print("###\t\t\t" + '{:243}'.format(text) + "###")
        sys.stdout.write(Fore.CYAN)

    @staticmethod
    def line(text):
        sys.stdout.write(Fore.BLUE)
        print('{:#<243}'.format("#"))
        sys.stdout.write(Fore.CYAN)

    @staticmethod
    def succes(text):
        sys.stdout.write(Fore.GREEN)
        sys.stdout.write('{:^300}'.format(text))
        sys.stdout.write(Fore.CYAN)

    @staticmethod
    def error(text):
        sys.stdout.write(Fore.RED)
        sys.stdout.write('{:^300}'.format(text))
        sys.stdout.write(Fore.CYAN)


