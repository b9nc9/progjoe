#!/usr/bin/env python

def caesar(be, k, d, d2):
    return ''.join(d.get(str((int(d2.get(x))+int(k))%len(d))) for x in be)

d = {   '0' : 'A',
        '1' : 'B',
        '2' : 'C',
        '3' : 'D',
        '4' : 'E',
        '5' : 'F',
        '6' : 'G',
        '7' : 'H',
        '8' : 'I',
        '9': 'J',
        '10': 'K',
        '11': 'L',
        '12': 'M',
        '13': 'N',
        '14': 'O',
        '15': 'P',
        '16': 'Q',
        '17': 'R',
        '18': 'S',
        '19': 'T',
        '20': 'U',
        '21': 'V',
        '22': 'W',
        '23': 'X',
        '24': 'Y',
        '25': 'Z',
        '26': '0',
        '27': '1',
        '28': '2',
        '29': '3',
        '30': '4',
        '31': '5',
        '32': '6',
        '33': '7',
        '34': '8',
        '35': '9',
        '36': ' ' }

d2 = {
        'A':'0',
        'B':'1',
        'C':'2',
        'D':'3',
        'E':'4',
        'F':'5',
        'G':'6',
        'H':'7',
        'I':'8',
        'J':'9',
        'K':'10',
        'L':'11',
        'M':'12',
        'N':'13',
        'O':'14',
        'P':'15',
        'Q':'16',
        'R':'17',
        'S':'18',
        'T':'19',
        'U':'20',
        'V':'21',
        'W':'22',
        'X':'23',
        'Y':'24',
        'Z':'25',
        '0':'26',
        '1':'27',
        '2':'28',
        '3':'29',
        '4':'30',
        '5':'31',
        '6':'32',
        '7':'33',
        '8':'34',
        '9':'35',
        ' ':'36',     
        }

be = input("Titkosítandó szöveg: ")
k = input("Kulcs: ")
print(caesar(be, int(k), d, d2))
