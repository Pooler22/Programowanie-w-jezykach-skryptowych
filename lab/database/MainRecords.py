import urllib.request

def load_from_url(url, file_name):
    return urllib.request.urlopen(url + file_name).read().decode('utf-8').split('\n')

path = "http://mmajchr.kis.p.lodz.pl/pwjs/"
files = ("imiona.txt","nazwiska.txt")

def exercise6a():
    for file in files:
        data = load_from_url(path, file)
        for i in sorted(data):
            print(i)
        print(data.__len__())

def exercise6b():
    names = load_from_url(path, files[0])
    surnames = load_from_url(path, files[1])