from lab.database.DatabaseExt import DatabaseExt
from lab.database.Menu import Menu

db = DatabaseExt()

menu = Menu()
menu.add_option("Ladowanie bazy danych o okreslonej nazwie.", db.load_ext)
menu.add_option("Ladowanie bazy danych z pliku.", db.load_from_file_ext)
menu.add_option("Ladowanie bazy danych z URL.", db.load_from_url_ext)
menu.add_option("Zapisywanie bazy danych do pliku o okreslonej nazwie.", db.save_ext)
menu.add_option("Dodawanie nowych wpisow do bazy danych", db.add_record_ext)
menu.add_option("Usuwanie wpisow z bazy danych", db.remove_record_ext)
menu.add_option("Wyswietlanie zawartosci bazy danych", db.open_db_ext)
#menu.add_option("Wyswietl posortowane wg imion", db.load_from_file)
#menu.add_option("Wyswietl posortowane wg nazwisk", db.load_from_file)
menu.add_option("Wyswietlanie listy opcji", menu.print)

menu.print()
menu.select_option()
