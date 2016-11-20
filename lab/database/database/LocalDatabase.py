import json
import os

from lab.database.database.AbstractDatabase import *


class LocalDatabase(objectAbstractClass):
    def __init__(self):
        super().__init__()

    def save(self,file_name, override=False):
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

    def load(self, file_name, separator):
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

    def show(self):
        for (key, value) in self.base:
            print(str(key) + " " + str(value))