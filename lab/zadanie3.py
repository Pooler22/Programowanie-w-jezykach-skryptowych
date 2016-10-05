"""
Na bazie zadania 2 dodac do skryptu mozliwosc obslugi "bazy danych" w pliku.
Skrypt powinien obslugiwac:
1) Ladowanie "bazy danych" z pliku o okreslonej nazwie.
2) Zapisywanie "bazy danych" do pliku o okreslonej nazwie.
3) Dodawanie nowych wpisow do "bazy danych".
4) Usuwanie wpisow z "bazy danych".
5) Wyswietlanie zawartosci "bazy danych".
6) Wyswietlanie listy "opcji"
"""

import pickle


class BazaDanych:
    def __init__(self):
        self.base = []
        self.base_name = ""
        self.menu1 = [
            '1) Ładowanie "bazy danych" z pliku o okreslonej nazwie.',
            '2) Zapisywanie "bazy danych" do pliku o okreslonej nazwie.',
            '3) Dodawanie nowych wpisow do "bazy danych".',
            '4) Usuwanie wpisow z "bazy danych".',
            '5) Wyswietlanie zawartosci "bazy danych".',
            '6) Wyswietlanie listy "opcji"'
        ]
        self.open_help()

    def load_db(self, file_name=""):
        if file_name == "":
            if self.base_name == "":
                print("Error: podaj nazwę bazy")
                return self.load_db(input('Ładowanie: Nazwa bazy danych: '))
            else:
                print("Logowanie do bazy", self.base_name)
                self.base_name = self.base_name
        else:
            print("Logowanie do ", file_name)
            self.base_name = file_name

        with open(self.base_name, 'rb') as f:
            self.base = pickle.load(f)
        print(self.base)
        self.check_wrapper()

    def save_db(self, file_name=""):
        if file_name == "":
            if self.base_name == "":
                print("Error: podaj nazwę bazy")
                return self.load_db(input('Zapisywanie: Nazwa bazy danych: '))
            else:
                print("Zapisywanie do bazy", self.base_name)
        else:
            print("Zapisywanie do ", file_name)
            self.base_name = file_name

        with open(self.base_name, 'wb') as f:
            pickle.dump(self.base, f)

        self.check_wrapper()

    def add_record(self, record):
        print("nowy rekord ", record)
        splited_record = record.split(' ')
        self.base.append({'name': splited_record[0], 'surname': splited_record[1]})
        print('Zapisano nowy rekord')

        self.check_wrapper()

    def remove_record(self, record):
        print("usuwanie rekord ", record)

        self.check_wrapper()

    def open_db(self):
        print("Wyświetl baze ")
        print(self.base)

        self.check_wrapper()

    def open_help(self):
        print('############################################################')
        for a in self.menu1:
            print(a)
        print('############################################################')

        self.check_wrapper()

    def check_wrapper(self):
        self.check(int(input('Podaj nr opcji:')))

    def check(self, number):
        if number == 1:
            self.load_db(input('Ładowanie: Nazwa bazy danych: '))
        elif number == 2:
            self.save_db(input('Zapis: Nazwa bazy danych: '))
        elif number == 3:
            self.add_record(input('Dodawanie rekordu: Imię i nazwisko: '))
        elif number == 4:
            self.remove_record(input('Usówanie rekordu: Immię i nazwisko: '))
        elif number == 5:
            self.open_db()
        elif number == 6:
            self.open_help()


BazaDanych()
