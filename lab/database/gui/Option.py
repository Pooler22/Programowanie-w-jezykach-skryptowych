class Option:
    def __init__(self, id_in, text, function):
        self.id = id_in
        self.text = text
        self.function = function

    def __str__(self):
        return str(self.id) + " " + self.text
