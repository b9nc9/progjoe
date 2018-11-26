#!/usr/bin/env python
import re

emailek = ""
minta =  r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)" #https://emailregex.com/

with open('emailek.txt', 'r') as f:
    emailek = f.read().splitlines()
f.close()

for x in emailek:
    if(x == '0'):
        break
    print("ÉRVÉNYES") if re.match(minta, x) else print ("NEM ÉRVÉNYES")

