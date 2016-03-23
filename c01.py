#!/bin/python3

import lib.data as data

d = data.Data(
        b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        ).fromhex()

def run():
    print( d.tob64() )

run()
