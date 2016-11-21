import urllib.request

def load_from_url(url, file_name):
    return urllib.request.urlopen(url + file_name).read().decode('utf-8').split('\n')

path = "http://mmajchr.kis.p.lodz.pl/pwjs/"

files = ("imiona.txt","nazwiska.txt")

for file in files:
    data = load_from_url(path, file)
    for i in sorted(data):
        print(i)
    print(data.__len__())
