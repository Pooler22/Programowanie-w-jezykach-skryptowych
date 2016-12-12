import sys, os
from time import sleep
from colorama import init


init()
from colorama import Fore, Back


class AwesomeEffects:
    def __init__(self):
        self.chromalog = None
        self.colorFore = Fore.CYAN
        self.colorBack = Back.WHITE
        self.info("tests")
        self.clean()

    def clean(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def progress(self):
        for i in range(51):
            sys.stdout.write('\r')
            sys.stdout.write("%-10s %d%%" % ('\u2588' * i, 2 * i))
            sys.stdout.flush()
            sleep(0.03)
        sys.stdout.write('\n')

    def normal(self, text):
        self.print_ext(Fore.CYAN, text)

    def info(self, text):
        self.print_ext(Fore.BLUE, text)

    def line(self, text):
        tmp0 = text * 64
        sys.stdout.write(Fore.BLUE)
        sys.stdout.write(self.colorBack)
        tmp1 = '{:60}'.format(tmp0)
        tmp2 = '{:^' + str(self.get_window_size()[0]) + '}'
        sys.stdout.write(tmp2.format(tmp1) + '\n')
        sys.stdout.write(Fore.BLUE)

    def success(self, text):
        self.print_ext(Fore.GREEN, text)

    def error(self, text):
        self.print_ext(Fore.RED, text)


    def print_ext(self, color, text):
        sys.stdout.write(color)
        sys.stdout.write(self.colorBack)
        tmp1 = '| '+'{:60}'.format(text)+' |'
        tmp2 = '{:^'+str(self.get_window_size()[0])+'}'
        sys.stdout.write(tmp2.format(tmp1) + '\n')
        sys.stdout.write(self.colorFore)

    @staticmethod
    def get_window_size():
        from ctypes import windll, create_string_buffer
        h = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
        if res:
            import struct
            (bufx, bufy, curx, cury, wattr,
             left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
            sizex = right - left + 1
            sizey = bottom - top + 1
        else:
            sizex, sizey = 80, 25  # can't determine actual size - return default values

        return sizex, sizey

