from lab.database.Database import Database
from lab.database.AwesomeEffects import AwesomeEffects

# import urllib.request
# url = 'http://example.com/'
# response = urllib.request.urlopen(url)
# data = response.read()
# text = data.decode('utf-8')
# print(text)


# name = input("Your name, sir/madam? ")
# while not name:
#     print("You must give some name")
#     name = input("Your name, sir/madam? ")
# if name.title() != "Bill Gates":
#     print("Welcome!")
# else:
#     print("Access denied")


class DatabaseExt(Database):
    # def __init__(self):
    #     Database().__init__()

    def save_ext(self):
        file = input("Wprowadz nazwe pliku")
        if file == "":
            AwesomeEffects.error("Brak podanej nazwy pliku")
            return
        else:
            if self.save(file):
                AwesomeEffects.succes("Dane zostaly zapisane")
            else:
                AwesomeEffects.error("Dane nie zostaly zapisane, istnieje już plik o takiej nazwie")
                if input("Nadpisac? (Y/N)") == "Y":
                    if self.save(file, True):
                        AwesomeEffects.succes("Dane zostaly zapisane, plik nadpisany")
                    else:
                        AwesomeEffects.error("Dane nie zostaly zapisane, plik nie nadpisany")

    def load_ext(self):
        file = input("Wprowadz nazwe pliku")
        if file == "":
            AwesomeEffects.error("Brak podanej nazwy pliku")
            return
        else:
            if self.load(file):
                AwesomeEffects.succes("Dane zostaly wczytane")
            else:
                AwesomeEffects.error("Dane nie zostaly wczytane")

    def load_from_file_ext(self):
        file = input("Wprowadz nazwe pliku")
        separator = input("Wprowadz rodzaj separatora (np przecinek)")
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
            AwesomeEffects.succes("Dane zostaly wczytane, Wczytano " + result + " rekordow")

    def add_record_ext(self):
        name, surname = input("Podaj dane oddzielone przecinkiem w kolejnosci: imie,nazwisko")
        if self.add_record(name, surname):
            AwesomeEffects.succes("Rekord zostal dodany")
        else:
            AwesomeEffects.error("Niepoprawne dane, rekord nie zostal dodany")

    def remove_record_ext(self):
        id_in = input("Podaj ID rekordu do usuniecia")
        AwesomeEffects.progres()
        if self.remove_record(id_in):
            AwesomeEffects.succes("Rekord zostal usuniety")
        else:
            AwesomeEffects.error("Brak rekordu o podanym ID")

    def open_db(self):
        AwesomeEffects.info("Wyświetlam baze")
        [print(record) for record in self.base]