from abc import ABC, abstractmethod


class AbstractDatabase(ABC):
    @abstractmethod
    def __init__(self):
        self.base = {}
        self.file_name = ""

    @abstractmethod
    def save(self,file_name, override=False):
        print("save")

    @abstractmethod
    def load(self, file_name, separator):
        print("load")

    @abstractmethod
    def show(self):
        print("show")

    @staticmethod
    def jdefault(o):
        return o.__dict__


objectAbstractClass = AbstractDatabase







