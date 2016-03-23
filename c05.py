#!/bin/python3

import lib.data as data

in1 = data.Data(
        b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
        )

def run():
    print( (in1^data.Data(b"ICE")).tohex() )

run()
