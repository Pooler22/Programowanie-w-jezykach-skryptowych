import urllib.request
from lab.database.database.Database import Database

def load_from_url(url, file_name):
    return urllib.request.urlopen(url + file_name).read().decode('utf-8').split('\n')


path = "http://mmajchr.kis.p.lodz.pl/pwjs/"
files = ["imiona.txt", "nazwiska.txt"]


def exercise6a():
    for file in files:
        print("\n" + file)
        data = load_from_url(path, file)
        for i in sorted(data):
            print(i)
        print(data.__len__())


db = Database()

def exercise6b():
    names = load_from_url(path, files[0])
    surnames = load_from_url(path, files[1])
    for i in range(1, surnames.__len__()-1):
        db.add_record(names[(names.__len__() % i - 2)], surnames[i])
    db.open_db()





exercise6a()
exercise6b()