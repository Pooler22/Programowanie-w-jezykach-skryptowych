# todo: Na bazie zadania 2 dodac do skryptu mozliwosc obslugi "bazy danych" w pliku.
# todo: Skrypt powinien obslugiwac:
# todo: 1) Ladowanie "bazy danych" z pliku o okreslonej nazwie.
# todo: 2) Zapisywanie "bazy danych" do pliku o okreslonej nazwie.
# todo: 3) Dodawanie nowych wpisow do "bazy danych".
# todo: 4) Usuwanie wpisow z "bazy danych".
# todo: 5) Wyswietlanie zawartosci "bazy danych".
# todo: 6) Wyswietlanie listy "opcji"
# todo: Do zadania 3 wykorzystac plik tekstowy z danymi w nastepujacym formacie:
# todo: Wczytac liste zdalnie z pliku lista.txt.
# todo: Prosze zapewnic mozliwosc rozroznienia w bazie nowych i starych rekordow (w
# todo: celu uzupelnienia "pustych" pol) wczytywanych z pliku "nowego formatu".
# todo: Prosze zastosowac podmenu.
# todo: Prosze stworzyc obiekt (klase abstrakcyjna) posiadajacy opcje:
# todo: 1) Zapisywania listy do pliku
# todo: 2) Wczytywania listy z pliku
# todo: 3) Wyswietlania listy na ekranie
# todo: Z tego obiektu maja dziedziczyc dwa obiekty zapewniajace odpowiednio
# todo: implementacje tych operacji dla list "z pliku na dysku" (zadanie 3) i z pliku
# todo: "na stronie" (zadanie 4).
# todo: LosowÄ iloĹÄ obiektĂłw obu typĂłw dodaÄ do listy. NastÄpnie iterujÄc przez tÄ
# todo: listÄ wywoĹaÄ funkcjÄ (np zapisu) BEZ sprawdzania typu obiektu!!!
# todo: Przygotowac obiekt losowo generujacy liste obiektow z zadania 5 oraz drugi
# todo: obiekt, ktory generuje losowe elementy(dwoch rodzajow) i dodaje do jednego z
# todo: dwoch typow obiektow. Jeden z generatorow danych ma pobierac je z internetu.


import pickle


class Database:


    def __init__(self):
        self.base = {}
        self.name = ""

    def load_db(self, file_name):
        self.name = file_name
        with open(self.name) as f:
            self.base = pickle.load(f)
        return print(self.base)

    def load_file(self, file_name):
        self.name = file_name
        with open(self.name) as f:
            for line in f:
                self.add_record(line.replace(',', ' '))

    def save_db(self, file_name):
        self.name = file_name
        with open(self.name) as f:
            pickle.dump(self.base, f)

    def add_record(self, record):
        splited_record = record.split(' ')
        self.base[splited_record[0]] = splited_record[1]

    def remove_record(self, record):
        print("usuwanie rekord ", record)

    def open_db(self):
        return self.base.items()