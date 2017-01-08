import json
import os

from lab.database.gui.AwesomeEffects import AwesomeEffects
from lab.database.database.AbstractDatabase import *
from lab.database.database.AutoIncrement import *
from lab.database.database.Record import Record


class LocalDatabase(objectAbstractClass):
    def __init__(self):
        super().__init__()
        self.awesome_effects = AwesomeEffects()

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

    def load_from_file(self, file_name, separator):
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

    def add_record(self, name, surname, sddres="", email=""):
        if name == "" or surname == "":
            return False
        else:
            new_id = AutoIncrement.auto_increment(self.index).__next__()
            self.index += 1
            self.base[str(new_id)] = Record(name, surname, sddres, email)
            return True

    def open_db(self):
        if self.base == {}:
            self.awesome_effects.info("Lokalna Baza danych jest pusta")
        else:
            self.awesome_effects.info("Wyświetlam baze")
            for (key, value) in sorted(self.base.items()):
                self.awesome_effects.success(str(key) + " " + str(value))

    def get_data(self):
        return self.base


