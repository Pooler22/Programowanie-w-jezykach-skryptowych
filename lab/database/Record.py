class Record:
    def __init__(self, id_in, name, surname, number="", email=""):
        self.id = id_in
        self.name = name
        self.surname = surname
        self.number = number
        self.email = email

    def __eq__(self, other):
        return self.name.__eq__(other.name) and self.surname.__eq__(other.surname) and self.number.__eq__(other.number) and self.email.__eq__(other.email)

    def __ne__(self, other):
        return not self.__eq__(other)
