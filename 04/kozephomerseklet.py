#!/usr/bin/env python

from collections import OrderedDict

#sor: év#hónap#nap#óra#perc#-#hőmérséklet#páratartalom%
meres = {}
with open('meres.txt') as f:
    sorok = f.read().splitlines()
    for x in sorok:
        sor = x.split('#')
        kulcs = sor[0]+'-'+sor[1]+'-'+sor[2]
        if(kulcs not in meres):
            meres[kulcs] = []
        else:
            meres[kulcs].append(float(sor[6]))

ki = open("kimenet.txt", "w")

for x in sorted(meres.keys()):
    ki.write('{0} - {1:1.3f}\n'.format(x, sum(meres[x])/float(len(meres[x]))))
ki.close()
