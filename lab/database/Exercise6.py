import urllib.request
from lab.database.database.Database import Database

class Exercise6:
    def __init__(self):
        path = "http://mmajchr.kis.p.lodz.pl/pwjs/"
        files = ["imiona.txt", "nazwiska.txt"]
        db = Database()

    def load_from_url(self, url, file_name):
        return urllib.request.urlopen(url + file_name).read().decode('utf-8').split('\n')

    def exercise6a(self):
        for file in self.files:
            print("\n" + file)
            data = self.load_from_url(self.path, file)
            for i in sorted(data):
                print(i)
            print(data.__len__())

    def exercise6b(self,):
        names = self.load_from_url(self.path, self.files[0])
        surnames = self.load_from_url(self.path, self.files[1])
        for i in range(0, surnames.__len__()):
            print(i)
            # db.add_record(names[(names.__len__() % i - 2)], surnames[i])
        # db.open_db()
        # print(db.base.__len__())
