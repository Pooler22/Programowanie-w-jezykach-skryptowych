import json
import os
from lab.database.database.Database import *
from lab.database.database.AbstractDatabase import *


class RemoteDatabase(objectAbstractClass):
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

    def add_record(self, name, surname, sddres="", email=""):
        if name == "" or surname == "":
            return False
        else:
            new_id = AutoIncrement.auto_increment(self.index).__next__()
            self.index += 1
            self.base[str(new_id)] = Record(name, surname, sddres, email)
            return True

    def load_from_file(self, file_url, separator_data):
        separator_id = ')'
        if file_url == "":
            return False
        else:
            response = urllib.request.urlopen(file_url).read().decode('utf-8')
            self.index = 1
            for record in response.split('\n'):
                raw_data = record.split(separator_id)
                if raw_data.__len__() == 2:
                    data_splited = raw_data[1].split(separator_data)
                    if data_splited.__len__() == 2:
                        self.base[int(raw_data[0])] = Record(data_splited[0], data_splited[1])
                        self.index += 1
                    if data_splited.__len__() == 3:
                        self.base[int(raw_data[0])] = Record(data_splited[0], data_splited[1], data_splited[2])
                        self.index += 1
                    if data_splited.__len__() == 4:
                        self.base[int(raw_data[0])] = Record(data_splited[0], data_splited[1], data_splited[2], data_splited[3])
                        self.index += 1
            return self.index

    def open_db(self):
        if self.base == {}:
            self.awesome_effects.info("Zdalna Baza danych jest pusta")
        else:
            self.awesome_effects.info("Wyświetlam baze")
            for (key, value) in sorted(self.base.items()):
                self.awesome_effects.success(str(key) + " " + str(value))

    def get_data(self):
        return self.base
