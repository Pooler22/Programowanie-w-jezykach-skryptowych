import urllib.request
from lab.database.database.DatabaseExt import DatabaseExt
from lab.database.database.Database import Database
from lab.database.gui.AwesomeEffects import AwesomeEffects
import re


class Exercise6:
    def __init__(self):
        self.path = "http://mmajchr.kis.p.lodz.pl/pwjs/"
        self.files = ["imiona.txt", "nazwiska.txt"]
        self.awesome_effects = AwesomeEffects()
        self.db = DatabaseExt()

    @staticmethod
    def load_from_url(url, file_name):
        return urllib.request.urlopen(url + file_name).read().decode('utf-8').split('\n')

    def exercise6a(self):
        for file in self.files:
            print("\n" + file)
            data = self.load_from_url(self.path, file)
            for i in sorted(data):
                print(i)
            print(data.__len__())

    def exercise6b(self, ):
        names = self.load_from_url(self.path, self.files[0])
        surnames = self.load_from_url(self.path, self.files[1])
        for i in range(0, surnames.__len__() - 1):
            self.awesome_effects.success(str(i + 1) + ", " + names[i % names.__len__()] + ", " + surnames[i])

    def exercise6c(self, ):
        names = self.load_from_url(self.path, self.files[0])
        surnames = self.load_from_url(self.path, self.files[1])
        for i in range(0, surnames.__len__() - 1):
            self.db.add_record(names[i % names.__len__()], surnames[i])

    def save_data_from_exercise_6c(self):
        self.exercise6c()
        self.db.save_ext()

    def upload_data_from_exercise_6c(self):
        self.db.save_ext()

    def exercise6d(self, file_url):
        if file_url == "":
            return False
        else:
            response = urllib.request.urlopen(file_url).read().decode('utf-8')
            i = 0
            for line in response.split('komputer'):
                print(line)
            print(response.split('komputer').__len__() - 1)

    def exercise6f(self, file_url):
        if file_url == "":
            return False
        else:
            response = urllib.request.urlopen(file_url).read().decode('utf-8')
            i = 0
            print(max([line.__len__() for line in response.replace("\n"," ").split(" ")]))
            # print(response.split(' ').split('\n').__len__() - 1)


exe = Exercise6()
# exe.exercise6b()
exe.exercise6f("http://mmajchr.kis.p.lodz.pl/pwjs/hack.txt")
