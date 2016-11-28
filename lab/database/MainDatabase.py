import random
from lab.database.database.LocalDatabase import LocalDatabase
from lab.database.database.RemoteDatabase import RemoteDatabase


def generate_random_databases_objects_to_list():
    ld = LocalDatabase()
    rd = RemoteDatabase()
    stop = 10
    list_object = []
    for x in range(stop):
        if random.choice([True, False]):
            list_object.append(ld)
        else:
            list_object.append(rd)
    return list_object


def exercise5():
    [print(str(x.show()) + " " + str(type(x))) for x in generate_random_databases_objects_to_list()]


exercise5()


class DataGenerator:
    def __init__(self):
        self.remote_data = []
        self.local_data = []

    def generate_remote(self, max):
        pass

    def generate_local(self, max):
        pass


def exercise5_1():
    object_with_random_databases_objects = generate_random_databases_objects_to_list()
    object_data_generator = DataGenerator()

    object_data_generator.generate_local(10)
    object_data_generator.generate_remote(10)

    [print(a.show()) for a in object_data_generator.local_data]
    [print(a.show()) for a in object_data_generator.remote_data]
