# Wczytac liste zdalnie z pliku lista.txt.
# todo: Prosze zapewnic mozliwosc rozroznienia w bazie nowych i starych rekordow (w celu uzupelnienia "pustych" pol)
# wczytywanych z pliku "nowego formatu".
# todo: Prosze zastosowac podmenu.
# todo: Z tego obiektu maja dziedziczyc dwa obiekty zapewniajace odpowiednio implementacje tych operacji dla list
# "z pliku na dysku" (zadanie 3) i z pliku "na stronie" (zadanie 4). Losową ilość obiektów obu typów dodać do listy.
# Następnie iterując przez tą listę wywołać funkcję (np zapisu) BEZ sprawdzania typu obiektu!!!
# todo: Przygotowac obiekt losowo generujacy liste obiektow z zadania 5 oraz drugi
# obiekt, ktory generuje losowe elementy(dwoch rodzajow) i dodaje do jednego z
# dwoch typow obiektow. Jeden z generatorow danych ma pobierac je z internetu.
import json
import os.path
import urllib.request

from lab.database.database.AutoIncrement import *
from lab.database.database.Record import Record


class Database(AutoIncrement):
    def __init__(self):
        self.base = {}
        self.name = ""
        self.file_name = ""
        self.index = 0

    @staticmethod
    def jdefault(o):
        return o.__dict__

    def save(self, file_name, override=False):
        if os.path.isfile(file_name):
            if override:
                self.file_name = file_name
                with open(self.file_name, 'w') as fp:
                    json.dump(self, fp, default=self.jdefault)
                return True
            else:
                return False
        else:
            self.file_name = file_name
            with open(self.file_name, 'w') as fp:
                json.dump(self, fp, default=self.jdefault)
            return True

    def load(self, file_name):
        if os.path.isfile(file_name):
            self.file_name = file_name
            a = json.load(open(self.file_name, 'r'))
            b = json.loads(json.JSONEncoder().encode(a))
            self.index = a["index"]
            self.file_name = a["file_name"]
            self.name = a["name"]
            for (key, record) in b["base"].items():
                self.base[key] = Record(record["name"], record["surname"], record["number"], record["email"])
            return True
        else:
            return False

    def load_from_file(self, file_name, separator=','):
        if os.path.isfile(file_name):
            i = 0
            self.file_name = file_name
            for line in (open(self.file_name, 'r', encoding='utf-8')):
                name, surname, addres, email = line.split(separator)
                if name == "" or surname == "":
                    return 0
                else:
                    self.add_record(name, surname, addres, email)
                    i += 1
            return i
        else:
            return False

    def load_from_url(self, file_url, separator_id, separator_data):
        index = 0
        if file_url == "":
            return False
        else:
            response = urllib.request.urlopen(file_url).read().decode('utf-8')
            for record in response.split('\n'):
                index += 1
                id_in, data = record.split(separator_id)
                name, surname, addres, email = data.split(separator_data)
                self.base[id_in.strip()] = Record(name.strip(), surname.strip(), addres.strip(), email.strip())
            self.index = index
        return index

    def add_record(self, name, surname, sddres="", email=""):
        if name == "" or surname == "":
            return False
        else:
            new_id = AutoIncrement.auto_increment(self.index).__next__()
            self.index += 1
            self.base[str(new_id)] = Record(name, surname,sddres,email)
            return True

    def remove_record(self, id_in):
        if id_in in self.base:
            del self.base[id_in]
            return True
        else:
            return False

    def sort(self, column_name, reverse=False):
        [print(key + " " + str(record)) for (key, record) in sorted(self.base.items(), key=lambda x: x[1].__getattribute__(column_name))]

    def __eq__(self, other):
        return self.name.__eq__(other.name) and self.base.__eq__(other.base)

    def __ne__(self, other):
        return not self.__eq__(other)
