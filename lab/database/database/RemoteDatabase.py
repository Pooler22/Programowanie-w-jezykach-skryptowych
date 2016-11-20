from lab.database.database.AbstractDatabase import *


class RemoteDatabase(objectAbstractClass):
    def __init__(self):
        super().__init__()

    def save(self,file_name, override=False):
        print("works")

    def load(self, file_url, separator):
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
        return index

    def show(self):
        for (key, value) in self.base.items():
            print(str(key) + " " + str(value))