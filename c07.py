#!/bin/python3

from lib.data import Data
from lib import data
from Crypto.Cipher import AES

key = data.Data(b"YELLOW SUBMARINE")
in1 = data.fromfile("data/d7.txt").fromb64()

def run():
    cipher = AES.new(bytes(key), AES.MODE_ECB)
    out1 = cipher.decrypt( bytes(in1) )
    out2 = Data( out1[0:-out1[-1]] ) # Remove padding
    print( out2.toascii() )

run()
