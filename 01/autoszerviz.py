#!/usr/bin/env python

szolgaltatasok = {"Kerékcsere" : 2000, "Lengéscsillapító-mérés" : 3000, "Kisszerviz" : 1300, "Klímafertőtlenítés" : 1300, "Fékpofacsere" : 10800}
vegosszeg = 0
tetel = ""

while(tetel != "ZÁRÁS"):
    tetel = input(":")
    vegosszeg = vegosszeg + szolgaltatasok.get(tetel) if tetel != "ZÁRÁS" else print(vegosszeg)
