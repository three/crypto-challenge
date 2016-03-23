#!/bin/python3

import lib.data as data

in1 = data.Data(
        b"1c0111001f010100061a024b53535009181c"
        ).fromhex()
in2 = data.Data(
        b"686974207468652062756c6c277320657965"
        ).fromhex()

def run():
    print( (in1^in2).tohex() )

run()
