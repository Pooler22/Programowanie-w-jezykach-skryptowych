# todo: Na bazie zadania 2 dodac do skryptu mozliwosc obslugi "bazy danych" w pliku.
# todo: Skrypt powinien obslugiwac:
# todo: 1) Ladowanie "bazy danych" z pliku o okreslonej nazwie.
# todo: 2) Zapisywanie "bazy danych" do pliku o okreslonej nazwie.
# todo: 3) Dodawanie nowych wpisow do "bazy danych".
# todo: 4) Usuwanie wpisow z "bazy danych".
# todo: 5) Wyswietlanie zawartosci "bazy danych".
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
import itertools
from lab.database.Record import Record


class Database:

    def __init__(self):
        self.base = []
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

    @staticmethod
    def auto_increment(start_in=0, step_in=1):
        i = start_in
        while True:
            yield i
            i += step_in

    def save(self, file_name):
        self.file_name = file_name
        json.dump((self.name, self.base), open(self.file_name, 'w'))

    def load(self, file_name):
        self.file_name = file_name
        self.name, self.base = json.load(open(self.file_name, 'r'))

    def load_from_file(self, file_name, separator=','):
        self.file_name = file_name
        for line in (open(self.file_name, 'r', encoding='utf-8')):
            name, surname = line.split(separator)
            self.add_record(name, surname)

    def add_record(self, name, surname):
        new_id = self.auto_increment()
        self.base.append(Record(new_id, name, surname))
        # self.base[name] = surname

    def remove_record(self, id_in):
        del self.base[id_in]

    def __eq__(self, other):
        return self.name.__eq__(other.name) and self.base.__eq__(other.base)

    def __ne__(self, other):
        return not self.__eq__(other)
