import lab.database.gui.Menu
from lab.database.database.DatabaseExt import DatabaseExt
from lab.database.gui.AwesomeEffects import AwesomeEffects

db = DatabaseExt()
menu = lab.database.gui.Menu.Menu("Menu: Glowne")
menu.add_graphic("""                                                                                                       ____                                                                                                                                         ###
###                                                                                                                   _.-'78o `"`--._                                                                                                                          ###
###                                                                                                               ,o888o.  .o888o,   ''-.                                                                                                                      ###
###                                                                                                             ,88888P  `78888P..______.]                                                                                                                     ###
###                                                                                                           /_..__..----""        __.'                                                                                                                       ###
###                                                                                                            `-._       /""| _..-''                                                                                                                          ###
###                                                                                                                "`-----\  `\\                                                                                                                                ###
###                                                                                                                        |   ;.-""--..                                                                                                                       ###
###                                                                                                                        | ,8o.  o88. `.                                                                                                                     ###
###                                                                                                                        `;888P  `788P  :                                                                                                                    ###
###                                                                                                                 .o""-.|`-._         ./                                                                                                                     ###
###                                                                                                                 J88 _.-/    ";"-P----'                                                                                                                     ###
###                                                                                                                 `--'\`|     /  /                                                                                                                           ###
###                                                                                                                     | /     |  |                                                                                                                           ###
###                                                                                                                     \|     /   |00                                                                                                                         ###
###                                                                                                                      `-----`---'                                                                                                                           ###
""")
load_menu = lab.database.gui.Menu.Menu("Menu: Wczytywanie danych")
view_menu = lab.database.gui.Menu.Menu("Menu: Wyswietlanie danych")

menu.add_option("Wczytywanie danych ->", load_menu.init_menu)
menu.add_option("Zapisywanie bazy danych do pliku o okreslonej nazwie.", db.save_ext)
menu.add_option("Dodawanie nowych wpisow do bazy danych", db.add_record_ext)
menu.add_option("Usuwanie wpisow z bazy danych", db.remove_record_ext)
menu.add_option("Wyswietlanie danych ->", view_menu.init_menu)
menu.add_option("Sortowanie", db.sort_ext)
menu.add_option("Wyswietlanie listy opcji", menu.print)

load_menu.add_option("Wczytywanie bazy danych o okreslonej nazwie.", db.load_ext)
load_menu.add_option("Wczytywanie bazy danych z pliku.", db.load_from_file_ext)
load_menu.add_option("Wczytywanie bazy danych z URL.", db.load_from_url_ext)
load_menu.add_option("Wyswietlanie listy opcji", load_menu.print)
load_menu.add_option("Wroc", menu.init_menu)

view_menu.add_option("Wyswietlanie zawartosci bazy danych", db.open_db_ext)
view_menu.add_option("Wyswietlanie rekorów bez wszystkich danych", db.open_incomplete_records_ext)
view_menu.add_option("Wyswietlanie listy opcji", load_menu.print)
view_menu.add_option("Wroc", menu.init_menu)

menu.init_menu()

