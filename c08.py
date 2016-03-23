#!/bin/python3

from lib import data
from lib.data import Data
from Crypto.Cipher import AES

in1 = [ x.fromhex() for x in data.fromfile("data/d8.txt").split(b'\n') ]

def run():
    cipher = AES.new(b"YELLOW SUBMARINE", AES.MODE_ECB)
    for t in in1:
        c = t.chunk( AES.block_size )
        if hasdups(c):
            print(t)

def hasdups(c):
    for n in range( len(c) ):
        for i in range(n+1, len(c)):
            if c[i] == c[n]:
                return True
    return False

run()
