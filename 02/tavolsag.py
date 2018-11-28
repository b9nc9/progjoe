#!/usr/bin/env python

from math import sqrt, sin, cos, atan2, radians

def tavolsag(p1h, p1sz, p2h, p2sz): #https://www.movable-type.co.uk/scripts/latlong.html
    sz = p2sz-p1sz
    h = p2h-p1h
    a = sin(sz/2)**2+cos(p1sz)*cos(p2sz)*sin(h/2)**2
    c = 2*atan2(sqrt(a), sqrt((1-a)))
    return 6371*c

p1sz = input("Szélesség: ")
p1h = input("Hosszúság: ")
p2sz = input("Szélesség: ")
p2h = input("Hosszúság: ")
print(tavolsag(radians(float(p1h[:-1])), radians(float(p1sz[:-1])), radians(float(p2h[:-1])), radians(float(p2sz[:-1]))))
