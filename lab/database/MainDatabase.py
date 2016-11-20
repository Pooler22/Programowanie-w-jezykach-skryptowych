import random
from lab.database.database.LocalDatabase import LocalDatabase
from lab.database.database.RemoteDatabase import RemoteDatabase

ld = LocalDatabase()
rd = RemoteDatabase()

stop = 5
list_object = []
for x in range(stop):
    if random.choice([True, False]):
        list_object.append(ld)
    else:
        list_object.append(rd)

[print(x.show()) for x in list_object]
