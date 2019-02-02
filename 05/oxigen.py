#!/usr/bin/env python

import operator

# eredemeny.txt
# SOR: rajtszám:név#nem(F vagy N)#első kör ideje#második kör ideje#harmadik kör ideje (ha van)#negyedik kör ideje(ha van).
class Versenyzo:
    def __init__(self, sor):
        self.rajtszam = sor.split(':')[0]
        adatok = sor.split(':', 1)[1].split('#')
        self.nev = adatok[0]
        self.nem = adatok[1]
        self.elso = int((adatok[2].split(':')[0]))*60+int(adatok[2].split(':')[1])
        self. masodik = int((adatok[3].split(':')[0]))*60+int(adatok[3].split(':')[1])
        self.osszido = self.elso+self.masodik
        if(len(adatok) == 6):
            self.harmadik = int((adatok[4].split(':')[0]))*60+int(adatok[4].split(':')[1])
            self.negyedik = int((adatok[5].split(':')[0]))*60+int(adatok[5].split(':')[1])
            self.osszido += self.harmadik+self.negyedik


def elsoHarom(szoveg, lista, nem):
    print(szoveg)
    n = 1
    for x in lista:
        if(x.nem == nem and n <= 3):
            print(x.nev + " " )
            n += 1
    print('\n')


tizkm = []
otkm = []

with open('eredmeny.txt') as f:
    sorok = f.read().splitlines()
    for x in sorok:
        if(len(x.split(':')) == 6):
            tizkm.append(Versenyzo(x))
        else:
            otkm.append(Versenyzo(x))

tizkm.sort(key=operator.attrgetter('osszido'))
otkm.sort(key=operator.attrgetter('osszido'))

elsoHarom("10km férfi: ", tizkm, 'F')
elsoHarom("10km női: ", tizkm, 'N')
elsoHarom('5km férfi: ', otkm, 'F')
elsoHarom('5km női: ', otkm, 'N')
