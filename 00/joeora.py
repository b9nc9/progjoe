#!/usr/bin/env python

d = [6*3, 2*3, 5*3, 5*3, 4*3, 5*3, 6*3, 3*3, 7*3, 6*3]
ido = input("Idő: ")

print(str(4+d[int(list(ido.split(':')[0])[0])]+d[int(list(ido.split(':')[0])[1])]+d[int(list(ido.split(':')[1])[0])]+d[int(list(ido.split(':')[1])[1])]) + " egység áramot fogyaszt el.") 
