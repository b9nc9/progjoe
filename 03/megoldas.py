#!/usr/bin/env python

'''OLVASS EL

A harmadik feladatot nem teljesen értettem, mert az URL csak egy string, és ha egy stringnek NULL-tól különböző értéke van, akkor az hamis nem lehet. Így az igaz stringet negálva false-t kapunk, ami 0, karakterként 0.
Ebben nem voltam biztos, mert a JavaScript szerepelt a leírásban és ahhoz nem értek egyáltalán. (Azt hittem, hogy ott valami menő varázslat történik majd.

Emiatt átugrottam a harmadik feladatot és brute forceoltam a titkosított szöveg első sorát és a kimenetből kerestem egy string-et, amit magyarul megértek. Mivel ez a boldog volt (oh, váratlan), így már csak ki kellett írnom a számot, amivel negálva az unicode karaktereket boldog-ot kaptam.
A kulcs az unicode 48 volt, ami 0....
'''

'''
Brute force



elso = [ord(c) for c in 'r_\T_W']

szo = ""
for y in range(0,128):
    for x in elso:
        szo += chr(y ^ x)
    if(szo == "Boldog"):
        print(y)
    szo = ""
'''

titkos = "r_\T_W [QBQSC_^ID yBZ UWI U]QY\D ]UBD QJ U\C_ ]UW_\T_ QZQ^T?[_D YC [Q@"
for x in titkos:
    print(chr(48 ^ ord(x)), end='')
