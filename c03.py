#!/bin/python3

import lib.data as data
import lib.english as english

in1 = data.Data(
        b"1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
        ).fromhex()

def run():
    top = english.findhigh(
            [ in1^[x] for x in range(256) ]
            )
    print("Best Score using XOR "+str(top[2])+":")
    print( str(top[0]) +" "+ str(top[1]) )

run()
