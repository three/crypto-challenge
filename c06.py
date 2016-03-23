#!/bin/python3

import lib.data as data
import lib.english as english

in1 = data.fromfile("data/d6.txt").fromb64()

def run():
    print(" === Preliminaries === ")
    print("Hamming test:")
    print("  ", data.Data(b"this is a test").hammingbits(b"wokka wokka!!!") )
    print(" === START === ")
    print(" = Searching for KEYSIZE = ")
    keysize_scores = [ (s, scorekeysize(s)) for s in range(2,40) ]
    keysizes = sorted(
            keysize_scores,
            key = lambda k: k[1]
            )
    print( keysizes )
    print(" = Searching for KEY =  ")
    for i in range(1): # Used for testing
        keysize = keysizes[i][0]
        print("Testing keysize: ",keysize)
        key = findkey( keysize )
        print( key )
        print( (in1^key).toascii() )

def findkey( keysize ):
    trans = in1.transpose(keysize)
    key = data.Data( keysize )
    for i in range(keysize):
        key[i] = english.findhigh([ trans[i]^[x] for x in range(256) ])[2]
    return key

def scorekeysize(keysize):
    chunks = in1.chunk(keysize)
    t1 = float( chunks[0].hammingbits( chunks[1] ) )
    t2 = float( chunks[2].hammingbits( chunks[3] ) )
    t3 = float( chunks[4].hammingbits( chunks[5] ) )
    t4 = float( chunks[6].hammingbits( chunks[7] ) )
    # Smaller keysizes are less likely so we "over-normalize"
    return (t1+t2+t3+t4)/keysize**(1.2)

run()
