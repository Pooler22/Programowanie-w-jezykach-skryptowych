"""
Wczytac liczbe n. Wczytac liste n imion i nazwisk (w jednej lini imie i
nazwisko). Wyswietlic "menu":
1 - Sortowanie wg imion
2 - Sortowanie wg nazwisk
Wczytaj od uzytkownika wybor (1 lub 2) i wyswietlic odpowiednio posortowana
liste.
"""


class Sort:
    @staticmethod
    def sortowanie():
        n = input('Podaj liczbe n: ')
        dict1 = {}

        print("Podaj imiona i nazwiska: (w jednej lini imie inazwisko)")
        for index in range(int(n)):
            tmp = input().split(' ')
            dict1[tmp[0]] = tmp[1]

        print("1 - Sortowanie wg imion")
        print("2 - Sortowanie wg nazwisk")
        sort = input()

        if sort == '1':
            Sort.sort_by_name(dict1)
        elif sort == '2':
            Sort.sort_by_surname(dict1)

    @staticmethod
    def sort_by_name(dict1):
        [print("Imie: %s Nazwisko: %s" % (key, values)) for key, values in sorted(dict1.items())]

    @staticmethod
    def sort_by_surname(dict1):
        [print("Imie: %s Nazwisko: %s" % (key, values)) for key, values in sorted(dict1.items(), key=lambda x: x[1])]


Sort.sortowanie()
