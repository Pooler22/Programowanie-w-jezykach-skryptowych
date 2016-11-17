"""
Prosze napisac skrypt, ktory wyswietla 8 kolejnych poteg liczby 2 (zaczynajac
od 2 do potegi 1), a nastepnie wczytuje 5 kolejnych poteg liczby 3 i sprawdza,
czy uzytkownik podal poprawna wartosc przy kazdym kroku. Po wpisaniu zlej
odpowiedzi program informuje o tym i konczy dzialanie (Nie pyta dalej!).
"""

for x in range(1, 8 + 1):
    print('2 ^', x, '=', 2 ** x)

for x in range(1, 5 + 1):
    print('3 ^', x, '= ?')
    answer = int(input())
    if 3 ** x == answer:
        print('good job')
    else:
        print('wrong answer')
        break
