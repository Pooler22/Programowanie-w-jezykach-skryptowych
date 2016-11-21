from lab.database.database.Database import Database
from lab.database.gui.AwesomeEffects import AwesomeEffects


class DatabaseExt(Database):
    def __init__(self):
        super().__init__()

    def save_ext(self):
        AwesomeEffects.info("Wprowadz nazwe pliku")
        file = input()
        if file == "":
            AwesomeEffects.error("Brak podanej nazwy pliku")
            return
        else:
            if self.save(file):
                AwesomeEffects.succes("Dane zostaly zapisane")
            else:
                AwesomeEffects.error("Dane nie zostaly zapisane, istnieje już plik o takiej nazwie")
                AwesomeEffects.info("Nadpisac? (Y/N)")
                if input() == "Y":
                    if self.save(file, True):
                        AwesomeEffects.succes("Dane zostaly zapisane, plik nadpisany")
                    else:
                        AwesomeEffects.error("Dane nie zostaly zapisane, plik nie nadpisany")

    def load_ext(self):
        AwesomeEffects.info("Wprowadz nazwe pliku")
        file = input()
        if file == "":
            AwesomeEffects.error("Brak podanej nazwy pliku")
            return
        else:
            if self.load(file):
                AwesomeEffects.succes("Dane zostaly wczytane")
            else:
                AwesomeEffects.error("Dane nie zostaly wczytane")

    def load_from_file_ext(self):
        AwesomeEffects.info("Wprowadz nazwe pliku")
        file = input()
        AwesomeEffects.info("Wprowadz rodzaj separatora (np przecinek)")
        separator = input()
        if file == "":
            AwesomeEffects.error("Brak podanej nazwy pliku")
            return
        elif separator == "":
            result = self.load_from_file(file)
        else:
            result = self.load_from_file(file, separator)

        if not result:
            AwesomeEffects.error("Dane nie zostaly wczytane")
        elif result == 0:
            AwesomeEffects.succes("dane nie zostaly wczytane, bledny format danych")
        else:
            AwesomeEffects.succes("Dane zostaly wczytane, Wczytano " + str(result) + " rekordow")

    def load_from_url_ext(self):
        AwesomeEffects.info("Podaj url (domyslnie link z tresci zadania)")
        url = input("")
        if url == "":
            url = "http://mmajchr.kis.p.lodz.pl/pwjs/zadania/lista.txt"
        AwesomeEffects.info("Podaj  separtor id od danych (domyslnie: ) )")
        separator_id = input()
        AwesomeEffects.info("Podaj separator miedzy danymi")
        separator_data = input()
        if separator_data == "":
            separator_data = ","
        if separator_id == "":
            separator_id = ")"
        result = self.load_from_url(url, separator_id, separator_data)
        if not result:
            AwesomeEffects.error("Nieprawidlowy URL, Danie nie wczytane")
        elif result == 0:
            AwesomeEffects.error("Nie wczytano zadnych danych")
        else:
            AwesomeEffects.succes("Plik zstal poprawnie wczytany, wczytano " + str(result) + " rekordow")

    def add_record_ext(self):
        AwesomeEffects.info("Podaj dane oddzielone spacja w kolejnosci: imie nazwisko")
        name, surname = input().split()
        if self.add_record(name, surname):
            AwesomeEffects.succes("Rekord zostal dodany")
        else:
            AwesomeEffects.error("Niepoprawne dane, rekord nie zostal dodany")

    def remove_record_ext(self):
        AwesomeEffects.info("Podaj ID rekordu do usuniecia")
        id_in = input()
        AwesomeEffects.progress()
        if self.remove_record(id_in):
            AwesomeEffects.succes("Rekord zostal usuniety")
        else:
            AwesomeEffects.error("Brak rekordu o podanym ID")

    def open_db_ext(self):
        if self.base == {}:
            AwesomeEffects.info("Baza danych jest pusta")
        else:
            AwesomeEffects.info("Wyświetlam baze")
            for (key, value) in self.base.items():
                print(str(key) + " " + str(value))

    def sort_ext(self):
        AwesomeEffects.info("Czy odwrocic sortowanie?(Y/N)")
        reverse = False
        if input() == "Y":
            reverse = True
        AwesomeEffects.info(
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
            AwesomeEffects.error("Nie rozpoznano nazwy atrybutu")
