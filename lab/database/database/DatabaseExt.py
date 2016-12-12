from lab.database.database.Database import Database
from lab.database.gui.AwesomeEffects import AwesomeEffects


class DatabaseExt(Database):
    def __init__(self, width=40):
        super().__init__()
        self.awesome_effects = AwesomeEffects(width)

    def save_ext(self):
        self.awesome_effects.info("Wprowadz nazwe pliku")
        file = input()
        if file == "":
            self.awesome_effects.error("Brak podanej nazwy pliku")
            return
        else:
            if self.save(file):
                self.awesome_effects.succes("Dane zostaly zapisane")
            else:
                self.awesome_effects.error("Dane nie zostaly zapisane, istnieje już plik o takiej nazwie")
                self.awesome_effects.info("Nadpisac? (Y/N)")
                if input() == "Y":
                    if self.save(file, True):
                        self.awesome_effects.succes("Dane zostaly zapisane, plik nadpisany")
                    else:
                        self.awesome_effects.error("Dane nie zostaly zapisane, plik nie nadpisany")

    def load_ext(self):
        self.awesome_effects.info("Wprowadz nazwe pliku")
        file = input()
        if file == "":
            self.awesome_effects.error("Brak podanej nazwy pliku")
            return
        else:
            if self.load(file):
                self.awesome_effects.succes("Dane zostaly wczytane")
            else:
                self.awesome_effects.error("Dane nie zostaly wczytane")

    def load_from_file_ext(self):
        self.awesome_effects.info("Wprowadz nazwe pliku")
        file = input()
        self.awesome_effects.info("Wprowadz rodzaj separatora (np przecinek)")
        separator = input()
        if file == "":
            self.awesome_effects.error("Brak podanej nazwy pliku")
            return
        elif separator == "":
            result = self.load_from_file(file)
        else:
            result = self.load_from_file(file, separator)

        if not result:
            self.awesome_effects.error("Dane nie zostaly wczytane")
        elif result == 0:
            self.awesome_effects.succes("dane nie zostaly wczytane, bledny format danych")
        else:
            self.awesome_effects.succes("Dane zostaly wczytane, Wczytano " + str(result) + " rekordow")

    def load_from_url_ext(self):
        self.awesome_effects.info("Podaj url (domyslnie link z tresci zadania)")
        url = input("")
        self.awesome_effects.info("Podaj  separtor id od danych (domyslnie: ) )")
        separator_id = input()
        self.awesome_effects.info("Podaj separator miedzy danymi")
        separator_data = input()

        if url.__len__() == 0:
            url = "http://mmajchr.kis.p.lodz.pl/pwjs/zadania/lista.txt"
        if separator_data.__len__() == 0:
            separator_data = ","
        if separator_id.__len__() == 0:
            separator_id = ")"
        result = self.load_from_url(url, separator_id, separator_data)
        if not result:
            self.awesome_effects.error("Nieprawidlowy URL, Danie nie wczytane")
        elif result == 0:
            self.awesome_effects.error("Nie wczytano zadnych danych")
        else:
            self.awesome_effects.succes("Plik zstal poprawnie wczytany, wczytano " + str(result) + " rekordow")

    def add_record_ext(self):
        self.awesome_effects.info("Podaj dane oddzielone spacja w kolejnosci: imie nazwisko")
        result = False
        in_data = input()
        data = in_data.split()

        if data.__len__() == 2:
            result = self.add_record(data[0], data[1])
        elif data.__len__() == 3:
            result = self.add_record(data[0], data[1], data[2])
        elif data.__len__() == 4:
            result = self.add_record(data[0], data[1], data[2], data[3])

        if result:
            self.awesome_effects.succes("Rekord zostal dodany")
        else:
            self.awesome_effects.error("Niepoprawne dane, rekord nie zostal dodany")

    def remove_record_ext(self):
        self.awesome_effects.info("Podaj ID rekordu do usuniecia")
        id_in = input()
        self.awesome_effects.progress()
        if self.remove_record(id_in):
            self.awesome_effects.succes("Rekord zostal usuniety")
        else:
            self.awesome_effects.error("Brak rekordu o podanym ID")

    def open_db_ext(self):
        if self.base == {}:
            self.awesome_effects.info("Baza danych jest pusta")
        else:
            self.awesome_effects.info("Wyświetlam baze")
            self.open_db()

    def open_incomplete_records_ext(self):
        self.awesome_effects.info("Wyswietlanie rekordow z danymi niekompletnymi")
        self.open_incomplete_records()

    def sort_ext(self):
        self.awesome_effects.info("Czy odwrocic sortowanie?(Y/N)")
        reverse = False
        if input() == "Y":
            reverse = True
        self.awesome_effects.info(
            "Podaj atrybut wzgledem ktorego odbedzie sie sortowanie \n1)name 2)surname 3)number 4)email)")
        column_name = input()
        if column_name == "1":
            self.sort("name", reverse)
        elif column_name == "2":
            self.sort("surname", reverse)
        elif column_name == "3":
            self.sort("number", reverse)
        elif column_name == "4":
            self.sort("email", reverse)
        else:
            self.awesome_effects.error("Nie rozpoznano nazwy atrybutu")
