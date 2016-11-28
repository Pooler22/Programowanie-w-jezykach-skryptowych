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
            self.index = 0
            self.file_name = file_name
            a = []
            a = json.load(open(self.file_name, 'r'))
            self.index = a["index"]
            self.file_name = a["file_name"]
            self.name = a["name"]

            b = json.loads(json.JSONEncoder().encode(a))
            for (key, record) in b["base"].items():
                self.base[int(key)] = Record(record["name"], record["surname"], record["number"], record["email"])
                self.index += 1
            return True
        else:
            return False

    def load_from_file(self, file_name, separator=','):
        if os.path.isfile(file_name):
            self.index = index = 0
            self.file_name = file_name
            for line in (open(self.file_name, 'r', encoding='utf-8')):
                name, surname, address, email = line.split(separator)
                if self.add_record(name, surname, address, email):
                    index += 1
            return index
        else:
            return False

    def load_from_url(self, file_url, separator_id=")", separator_data=","):
        index = 0
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

    def add_record(self, name, surname, address="", email=""):
        if name == "" or surname == "":
            return False
        else:
            self.base[int(AutoIncrement.auto_increment(self.index).__next__())] = Record(name, surname, address,email)
            self.index += 1
            return True

    def remove_record(self, id_in):
        if id_in in self.base:
            del self.base[id_in]
            return True
        else:
            return False

    def sort(self, column_name, reverse=False):
        [print(key + " " + str(record)) for (key, record) in
         sorted(self.base.items(), key=lambda x: x[1].__getattribute__(column_name))]

    def open_db(self):
        for (key, value) in sorted(self.base.items()):
            print(str(key) + " " + str(value))

    def open_incomplete_records(self):
        {print(str(key) + " " + str(record)) for key, record in sorted(self.base.items()) if record.is_incomplete_records()}

    def __eq__(self, other):
        return self.name.__eq__(other.name) and self.base.__eq__(other.base)

    def __ne__(self, other):
        return not self.__eq__(other)
