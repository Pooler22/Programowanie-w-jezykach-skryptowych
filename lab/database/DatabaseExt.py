import pickle
import sys
import lab.Database
#
# import urllib.request
# url = 'http://example.com/'
# response = urllib.request.urlopen(url)
# data = response.read()
# text = data.decode('utf-8')
# print(text)


class BazaDanych(lab.Database):
    def __init__(self):
        super().__init__()

        self.menu = [
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

    def load_db(self, file_name=""):
        if file_name == "":
            if self.name == "":
                print("Error: podaj nazwe bazy")
                return self.load_db(input('Ladowanie: Nazwa bazy danych: '))
            else:
                print("Logowanie do bazy", self.name)
                super().name = self.name
        else:
            print("Logowanie do ", file_name)
            super().name = file_name

        with open(self.name, 'rb') as f:
            super().base = pickle.load(f)
        print(self.base)
        self.check_wrapper()

    def load_file(self, file_name=""):
        if file_name == "":
            if self.name == "":
                print("Error: podaj nazwe bazy")
                return self.load_db(input('Ladowanie: Nazwa bazy danych: '))
            else:
                print("Logowanie do bazy", self.name)
                self.name = self.name
        else:
            print("Ladowanie z ", file_name)
            self.name = file_name

        with open(self.name, 'r') as f:
            for line in f:
                self.add_record(line.replace(',', ' '))
        self.check_wrapper()

    def save_db(self, file_name=""):
        if file_name == "":
            if self.name == "":
                print("Error: podaj nazwe bazy")
                return self.load_db(input('Zapisywanie: Nazwa bazy danych: '))
            else:

                print("Zapisywanie do bazy", self.name)
        else:
            print("Zapisywanie do ", file_name)
            self.name = file_name
        with open(self.name, 'wb') as f:
            pickle.dump(self.base, f)

        self.check_wrapper()

    def add_record(self, record):
        print("nowy rekord ", record)
        splited_record = record.split(' ')
        # self.base.({'name': splited_record[0], 'surname': splited_record[1]})
        self.base[splited_record[0]] = splited_record[1]
        print('Zapisano nowy rekord')
        self.check_wrapper()

    def remove_record(self, record):
        print("usuwanie rekord ", record)

        self.check_wrapper()

    def open_db(self):
        print("Wyświetlam baze ")
        print("Imie\t|\tNazwisko")
        for keys, values in self.base.items():
            print(keys, "\t|\t", values)
        # print(self.base_dict)

        self.check_wrapper()

    def open_help(self):
        sys.stdout.flush()
        print('     {:\u2588^70}'.format('\u2588'))
        print('     {:\u2588^70}'.format(' MyDB: Twoja  ulubiona aplikacja '))
        print('     {:\u2588^70}'.format('\u2588'))
        print('     {:\u2588^70}'.format('MENU'))
        print('     {:\u2588^70}'.format('\u2588'))
        for a in self.menu:
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
#            Sort.sort_by_name(self.base_dict)
            self.check_wrapper()
        elif number == 8:
#            Sort.sort_by_surname(self.base_dict)
            self.check_wrapper()
        elif number == 9:
            self.load_file(input('Ladowanie: Nazwa pliku: '))
            self.check_wrapper()


BazaDanych().open_help()
