# todo: Na bazie zadania 2 dodac do skryptu mozliwosc obslugi "bazy danych" w pliku.
# Skrypt powinien obslugiwac:
# 1) Ladowanie "bazy danych" z pliku o okreslonej nazwie.
# 2) Zapisywanie "bazy danych" do pliku o okreslonej nazwie.
# 3) Dodawanie nowych wpisow do "bazy danych".
# 4) Usuwanie wpisow z "bazy danych".
# 5) Wyswietlanie zawartosci "bazy danych".
# todo: 6) Wyswietlanie listy "opcji"
# todo: Do zadania 3 wykorzystac plik tekstowy z danymi w nastepujacym formacie:
# todo: Wczytac liste zdalnie z pliku lista.txt.
# todo: Prosze zapewnic mozliwosc rozroznienia w bazie nowych i starych rekordow (w
# todo: celu uzupelnienia "pustych" pol) wczytywanych z pliku "nowego formatu".
# todo: Prosze zastosowac podmenu.
# todo: Prosze stworzyc obiekt (klase abstrakcyjna) posiadajacy opcje:
# todo: 1) Zapisywania listy do pliku
# todo: 2) Wczytywania listy z pliku
# todo: 3) Wyswietlania listy na ekranie
# todo: Z tego obiektu maja dziedziczyc dwa obiekty zapewniajace odpowiednio
# todo: implementacje tych operacji dla list "z pliku na dysku" (zadanie 3) i z pliku
# todo: "na stronie" (zadanie 4).
# todo: LosowÄ iloĹÄ obiektĂłw obu typĂłw dodaÄ do listy. NastÄpnie iterujÄc przez tÄ
# todo: listÄ wywoĹaÄ funkcjÄ (np zapisu) BEZ sprawdzania typu obiektu!!!
# todo: Przygotowac obiekt losowo generujacy liste obiektow z zadania 5 oraz drugi
# todo: obiekt, ktory generuje losowe elementy(dwoch rodzajow) i dodaje do jednego z
# todo: dwoch typow obiektow. Jeden z generatorow danych ma pobierac je z internetu.

import json
import os.path
from lab.database.AutoIncrement import *
from lab.database.Record import Record


class Database(AutoIncrement):
    def __init__(self):
        self.base = {}
        self.name = ""
        self.file_name = ""

    # @property
    # def name(self):
    #     return self.name
    #
    # @name.setter
    # def name(self, value):
    #     self.name = value
    #
    # @name.deleter
    # def name(self):
    #     del self.name
    #
    # @property
    # def base(self):
    #     return self.base
    #
    # @base.setter
    # def base(self, value):
    #     self.base = value
    #
    # @base.deleter
    # def base(self):
    #     del self.base

    def save(self, file_name, override=False):
        if os.path.isfile(file_name) or not override:
            return False
        else:
            self.file_name = file_name
            json.dump((self.name, self.base), open(self.file_name, 'w'))
            return True

    def load(self, file_name):
        if os.path.isfile(file_name):
            self.file_name = file_name
            self.name, self.base = json.load(open(self.file_name, 'r'))
            return True
        else:
            return False

    def load_from_file(self, file_name, separator=','):
        if os.path.isfile(file_name):
            i = 0
            self.file_name = file_name
            for line in (open(self.file_name, 'r', encoding='utf-8')):
                name, surname = line.split(separator)
                if name == "" or surname == "":
                    return 0
                else:
                    self.add_record(name, surname)
                    i += 1
            return i
        else:
            return False

    def add_record(self, name, surname):
        if name == "" or surname == "":
            return False
        else:
            new_id = self.auto_increment()
            self.base[new_id] = Record(name, surname)
            return True

    def remove_record(self, id_in):
        if id_in in self.base:
            del self.base[id_in]
            return True
        else:
            return False

    def __eq__(self, other):
        return self.name.__eq__(other.name) and self.base.__eq__(other.base)

    def __ne__(self, other):
        return not self.__eq__(other)
