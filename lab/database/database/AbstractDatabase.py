from abc import ABC, abstractmethod


class AbstractDatabase(ABC):
    @abstractmethod
    def __init__(self,asd):
        self.base = {}
        self.file_name = ""

    @abstractmethod
    def save(self,file_name, override=False):
        pass

    @abstractmethod
    def load(self, file_name, separator):
        pass

    @abstractmethod
    def show(self):
        pass

    @staticmethod
    def jdefault(o):
        return o.__dict__


objectAbstractClass = AbstractDatabase







