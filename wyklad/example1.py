import operator


def sort1(in1):
    dict1 = dict(zip(in1, [x.split("@")[1].count(".") for x in in1]))
    return [k[0] for k in list(sorted(dict1.items(), key=operator.itemgetter(1)))]


tab = ["abc.xyz@serwer.o.bardzo.dlugiej.nazwie.com", "jan.kot@gmail.com", "dsan@kis.p.lodz.pl"]

print(sort1(tab))
