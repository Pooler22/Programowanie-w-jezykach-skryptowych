import random
from random import randint
from lab.database.database.LocalDatabase import LocalDatabase
from lab.database.database.RemoteDatabase import RemoteDatabase
from lab.database.gui.AwesomeEffects import AwesomeEffects

class Exercise5:
    def __init__(self):
        self.awesome_effects = AwesomeEffects()

    @staticmethod
    def generate_random_databases_objects_to_list(count=10):
        ld = LocalDatabase()
        rd = RemoteDatabase()
        list_object = []

        for x in range(count):
            if random.choice([True, False]):
                list_object.append(ld)
            else:
                list_object.append(rd)
        return list_object

    class DataGenerator:
        def __init__(self):
            pass
            ldb = LocalDatabase()
            rdb = RemoteDatabase()
            ldb.load_from_file("dane_lokalne.txt", ",")
            rdb.load_from_file("http://mmajchr.kis.p.lodz.pl/pwjs/zadania/lista.txt", ",")
            self.remote_data = ldb.get_data()
            self.local_data = rdb.get_data()

        def generate(self, db, count):
            if random.choice([True, False]):
                for record in [(self.remote_data[str(randint(1, self.remote_data.__len__() - 1))]) for x in range(count)]:
                    db.add_record(record.name, record.surname,record.email, record.number)
            else:
                for record in [(self.local_data[(randint(1, self.local_data.__len__() - 1))]) for x in range(count)]:
                    db.add_record(record.name, record.surname,record.email, record.number)

    def exercise5(self):
        [(x.open_db()) for x in self.generate_random_databases_objects_to_list(10)]

    def exercise5_1(self):
        count = 10
        object_with_random_databases_objects = self.generate_random_databases_objects_to_list(2)
        object_data_generator = self.DataGenerator()

        for element in object_with_random_databases_objects:
            object_data_generator.generate(element, 2)

        [a.open_db() for a in object_with_random_databases_objects]


# exe = Exercise5()
# exe.exercise5_1()
