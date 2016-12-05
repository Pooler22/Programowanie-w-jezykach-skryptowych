import json
import os
from lab.database.database.Database import *
from lab.database.database.AbstractDatabase import *


class RemoteDatabase(objectAbstractClass):
    def __init__(self):
        super().__init__()

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

    def load(self, file_url, separator):
        index = 0
        if file_url == "":
            return False
        else:
            response = urllib.request.urlopen(file_url).read().decode('utf-8')
            for record in response.split('\n'):
                index += 1
                id_in, data = record.split(")")
                name, surname, addres, email = data.split(",")
                self.base[id_in.strip()] = Record(name.strip(), surname.strip(), addres.strip(), email.strip())
            self.index = index
        return index

    def show(self):
        for (key, value) in self.base.items():
            AwesomeEffects.info(str(key) + " " + str(value))
