"""
    Na bazie zadania 2 dodac do skryptu mozliwosc obslugi "bazy danych" w pliku.
    Skrypt powinien obslugiwac:
    1) Ladowanie "bazy danych" z pliku o okreslonej nazwie.
    2) Zapisywanie "bazy danych" do pliku o okreslonej nazwie.
    3) Dodawanie nowych wpisow do "bazy danych".
    4) Usuwanie wpisow z "bazy danych".
    5) Wyswietlanie zawartosci "bazy danych".
    6) Wyswietlanie listy "opcji"

    Do zadania 3 wykorzystac plik tekstowy z danymi w nastepujacym formacie:
    Imie(znak nie bedacy bialem znakiem lub litera)Nazwisko

Wczytac liste zdalnie z pliku lista.txt.

Prosze zapewnic mozliwosc rozroznienia w bazie nowych i starych rekordow (w
celu uzupelnienia "pustych" pol) wczytywanych z pliku "nowego formatu".
Prosze zastosowac podmenu.

Prosze stworzyc obiekt (klase abstrakcyjna) posiadajacy opcje:
1) Zapisywania listy do pliku
2) Wczytywania listy z pliku
3) Wyswietlania listy na ekranie
Z tego obiektu maja dziedziczyc dwa obiekty zapewniajace odpowiednio
implementacje tych operacji dla list "z pliku na dysku" (zadanie 3) i z pliku
"na stronie" (zadanie 4).
LosowÄ iloĹÄ obiektĂłw obu typĂłw dodaÄ do listy. NastÄpnie iterujÄc przez tÄ
listÄ wywoĹaÄ funkcjÄ (np zapisu) BEZ sprawdzania typu obiektu!!!

Przygotowac obiekt losowo generujacy liste obiektow z zadania 5 oraz drugi
obiekt, ktory generuje losowe elementy(dwoch rodzajow) i dodaje do jednego z
dwoch typow obiektow. Jeden z generatorow danych ma pobierac je z internetu.

"""

import pickle
import sys


import urllib.request
url = 'http://example.com/'
response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')
print(text)

from colorama import init

init()
from colorama import Fore, Back, Style
from time import sleep
from zadanie2 import Sort





class Awesome:
    @staticmethod
    def progres():
        for i in range(51):
            sys.stdout.write('\r')
            sys.stdout.write("%-50s %d%%" % ('\u2588' * i, 2 * i))
            sys.stdout.flush()
            sleep(0.03)
        sys.stdout.write('\n')


class Rekord:
    def __init__(self, id_in, name, surname, number, email):
        self.id = id_in
        self.name = name
        self.surname = surname
        self.number = number
        self.email = email


class BazaDanych:
    def __init__(self):
        # self.base = []
        self.base_dict = {}
        self.base_name = ""
        self.menu1 = [
            '     \u2588    1)  Ladowanie "bazy danych" z pliku o okreslonej nazwie.        \u2588    ',
            '     \u2588    2)  Zapisywanie "bazy danych" do pliku o okreslonej nazwie.     \u2588    ',
            '     \u2588    3)  Dodawanie nowych wpisow do "bazy danych".                   \u2588    ',
            '     \u2588    4)  Usuwanie wpisow z "bazy danych".                            \u2588    ',
            '     \u2588    5)  Wyswietlanie zawartosci "bazy danych".                      \u2588    ',
            '     \u2588    6)  Wyswietlanie listy "opcji".                                 \u2588    ',
            '     \u2588    7)  Wyswietl posortowane wg imion                               \u2588    ',
            '     \u2588    8)  Wyswietl posortowane wg nazwisk                             \u2588    ',
            '     \u2588    9)  Ladowanie danych z pliku o okreslonej nazwie.               \u2588    ',
        ]
        self.open_help()

    def load_db(self, file_name=""):
        """
        Wczytuje baze danych z pliku
        :param file_name: nazwa istaniejacej bazy danych
        """
        if file_name == "":
            if self.base_name == "":
                print(Fore.RED)
                print("Error: podaj nazwe bazy")
                print(Fore.CYAN)
                return self.load_db(input('Ladowanie: Nazwa bazy danych: '))
            else:
                print("Logowanie do bazy", self.base_name)
                self.base_name = self.base_name
        else:
            print("Logowanie do ", file_name)
            self.base_name = file_name

        with open(self.base_name, 'rb') as f:
            self.base_dict = pickle.load(f)
        print(self.base_dict)
        self.check_wrapper()

    def load_file(self, file_name=""):
        """
        Wczytuje dane z pliku
        :param file_name: nazwa istaniejacej bazy danych
        """
        if file_name == "":
            if self.base_name == "":
                print("Error: podaj nazwe bazy")
                return self.load_db(input('Ladowanie: Nazwa bazy danych: '))
            else:
                print("Logowanie do bazy", self.base_name)
                self.base_name = self.base_name
        else:
            print("Ladowanie z ", file_name)
            self.base_name = file_name

        with open(self.base_name, 'r') as f:
            for line in f:
                self.add_record(line.replace(',', ' '))
        self.check_wrapper()

    def save_db(self, file_name=""):
        """
        Zaposuje baze danych w pliku
        :param file_name: nazwa bazy danych
        """
        if file_name == "":
            if self.base_name == "":
                print("Error: podaj nazwe bazy")
                return self.load_db(input('Zapisywanie: Nazwa bazy danych: '))
            else:

                print("Zapisywanie do bazy", self.base_name)
        else:
            print("Zapisywanie do ", file_name)
            self.base_name = file_name
        Awesome.progres()
        with open(self.base_name, 'wb') as f:
            pickle.dump(self.base_dict, f)

        self.check_wrapper()

    def add_record(self, record):
        print("nowy rekord ", record)
        splited_record = record.split(' ')
        # self.base.({'name': splited_record[0], 'surname': splited_record[1]})
        self.base_dict[splited_record[0]] = splited_record[1]
        Awesome.progres()
        print(Fore.GREEN)
        print('Zapisano nowy rekord')
        print(Fore.CYAN)
        self.check_wrapper()

    def remove_record(self, record):
        print("usuwanie rekord ", record)

        self.check_wrapper()

    def open_db(self):
        print("Wyświetlam baze ")
        print("Imie\t|\tNazwisko")
        for keys, values in self.base_dict.items():
            print(keys, "\t|\t", values)
        # print(self.base_dict)

        self.check_wrapper()

    def open_help(self):
        sys.stdout.flush()
        print(Fore.CYAN)
        print('     {:\u2588^70}'.format('\u2588'))
        print('     {:\u2588^70}'.format(' MyDB: Twoja  ulubiona aplikacja '))
        print('     {:\u2588^70}'.format('\u2588'))
        print('     {:\u2588^70}'.format('MENU'))
        print('     {:\u2588^70}'.format('\u2588'))
        for a in self.menu1:
            print(a)
        print('     {:\u2588^70}'.format('\u2588'))

        self.check_wrapper()

    def check_wrapper(self):
        self.check(int(input('Podaj nr opcji:')))

    @staticmethod
    def print_ext(text):
        print("#", text, "#")

    def check(self, number):
        if number == 1:
            self.load_db(input('Ladowanie: Nazwa bazy danych: '))
        elif number == 2:
            self.save_db(input('Zapis: Nazwa bazy danych: '))
        elif number == 3:
            self.add_record(input('Dodawanie rekordu: Imie i nazwisko: '))
        elif number == 4:
            self.remove_record(input('Usoanie rekordu: Immię i nazwisko: '))
        elif number == 5:
            self.open_db()
        elif number == 6:
            self.open_help()
        elif number == 7:
            Sort.sort_by_name(self.base_dict)
            self.check_wrapper()
        elif number == 8:
            Sort.sort_by_surname(self.base_dict)
            self.check_wrapper()
        elif number == 9:
            self.load_file(input('Ladowanie: Nazwa pliku: '))
            self.check_wrapper()


BazaDanych()
