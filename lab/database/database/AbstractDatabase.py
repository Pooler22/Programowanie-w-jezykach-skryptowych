from abc import ABC, abstractmethod


class AbstractDatabase(ABC):
    @abstractmethod
    def __init__(self):
        self.base = {}
        self.name = ""
        self.file_name = ""
        self.index = 0

    @abstractmethod
    def save(self, file_name, override=False):
        pass

    @abstractmethod
    def load_from_file(self, file_name, separator):
        pass

    @abstractmethod
    def open_db(self):
        pass

    @staticmethod
    def jdefault(o):
        return o.__dict__

    def get_data(self):
        return self.base


objectAbstractClass = AbstractDatabase
