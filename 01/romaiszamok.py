#!/usr/bin/env python

def ellenoriz(romai): #MINIMÁLIS ELLENŐRZÉS
    kovetkezo = romai[0]
    szamlal = 0
    for x in range(0, len(romai)):
        if(x+1 < len(romai)):
            kovetkezo = romai[x+1]
        karakter = romai[x]
        if(kovetkezo == karakter):
            szamlal+=1
        else:
            szamlal = 0
        if(szamlal > 3):
            return False
    return True

def konvarab(romai):
    arab = 0
    ertekek = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for x in range(0, len(romai)):
        kovetkezo = 0
        if(x+1 < len(romai)):
            kovetkezo = ertekek.get(romai[x+1])
        arab = arab + ertekek.get(romai[x]) if kovetkezo <= ertekek.get(romai[x]) else arab - ertekek.get(romai[x])
    return arab

romai = input("Római: ")
if(ellenoriz(romai)):
    print(konvarab(romai))
else:
    print("Hibás számot adtál meg.")
