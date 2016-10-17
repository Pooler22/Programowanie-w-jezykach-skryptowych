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


from zadanie2 import Sort


class BazaDanych:
    def __init__(self):
        #self.base = []
        self.base_dict = {}
        self.base_name = ""
        self.menu1 = [
            '     \u2588    1)  Ladowanie "bazy danych" z pliku o okreslonej nazwie.        \u2588    ',
            '     \u2588    2)  Zapisywanie "bazy danych" do pliku o okreslonej nazwie.     \u2588    ',
            '     \u2588    3)  Dodawanie nowych wpisow do "bazy danych".                   \u2588    ',
            '     \u2588    4)  Usuwanie wpisow z "bazy danych".                            \u2588    ',
            '     \u2588    5)  Wyswietlanie zawartosci "bazy danych".                      \u2588    ',
            '     \u2588    6)  Wyswietlanie listy "opcji".                                 \u2588    ',
            '     \u2588    7)  Wyświetl posortowane wg imion                               \u2588    ',
            '     \u2588    8)  Wyświetl posortowane wg nazwisk                             \u2588    ',
            '     \u2588    9)  Ladowanie danych z pliku o okreslonej nazwie.               \u2588    ',
        ]
        self.open_help()

    def load_db(self, file_name=""):
        """
        Wczytuje baze danych z pliku
        :param file_name: nazwa istaniejącej bazy danych
        """
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
            self.base_dict = pickle.load(f)
        print(self.base_dict)
        self.check_wrapper()

    def load_file(self, file_name=""):
        """
        Wczytuje dane z pliku
        :param file_name: nazwa istaniejącej bazy danych
        """
        if file_name == "":
            if self.base_name == "":
                print("Error: podaj nazwę bazy")
                return self.load_db(input('Ładowanie: Nazwa bazy danych: '))
            else:
                print("Logowanie do bazy", self.base_name)
                self.base_name = self.base_name
        else:
            print("Ladowanie z ", file_name)
            self.base_name = file_name

        with open(self.base_name, 'r') as f:
            for line in f:
                self.add_record(line.replace(',',' '))    
        self.check_wrapper()

    def save_db(self, file_name=""):
        """
        Zaposuje baze danych w pliku
        :param file_name: nazwa bazy danych
        """
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
            pickle.dump(self.base_dict, f)

        self.check_wrapper()

    def add_record(self, record):
        print("nowy rekord ", record)
        splited_record = record.split(' ')
        #self.base.({'name': splited_record[0], 'surname': splited_record[1]})
        self.base_dict[splited_record[0]] = splited_record[1]
        print('Zapisano nowy rekord')

        self.check_wrapper()

    def remove_record(self, record):
        print("usuwanie rekord ", record)

        self.check_wrapper()

    def open_db(self):
        print("Wyświetlam baze ")
        print("Imie\t|\tNazwisko")
        for keys,values in self.base_dict.items():
            print(keys,"\t|\t",values)
        #print(self.base_dict)

        self.check_wrapper()

    def open_help(self):
        print('     {:\u2588^70}'.format('\u2588'))
        print('     {:\u2588^70}'.format(' MyDB: Twoja  ulubiona aplikacja '))
        print('     {:\u2588^70}'.format('\u2588'))
        print('     {:\u2588^70}'.format(' '))
        print('     {:\u2588^70}'.format('\u2588'))
        for a in self.menu1:
            print(a)
        print('     {:\u2588^70}'.format('\u2588'))

        self.check_wrapper()

    def check_wrapper(self):
        self.check(int(input('Podaj nr opcji:')))

    def printExt(self,text):
        print("#",text,"#")
    
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
        elif number == 7:
            Sort.sort_by_name(self.base_dict)
            self.check_wrapper()
        elif number == 8:
            Sort.sort_by_surname(self.base_dict)
            self.check_wrapper()
        elif number == 9:
            self.load_file(input('Ładowanie: Nazwa pliku: '))
            self.check_wrapper()


BazaDanych()
