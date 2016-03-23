#!/bin/python3

import lib.data as data
import lib.english as english

def run():
    lines = [ x.fromhex() for x in  data.fromfile("data/d4.txt").split(b"\n") ]
    topscore = -100.
    topdata = None
    for l in lines:
        if len(l) < 1:
            continue
        for x in range(255):
            s = english.scorefull( l^data.Data([x]) )
            if s > topscore:
                topscore = s
                topdata = l^data.Data([x])
    print( topdata )

run()
